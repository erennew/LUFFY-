from aiohttp import web
from plugins import web_server
import time
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
import asyncio

from config import (
    API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS,
    FORCE_SUB_CHANNEL_1, FORCE_SUB_CHANNEL_2,
    FORCE_SUB_CHANNEL_3, FORCE_SUB_CHANNEL_4,
    CHANNEL_ID, PORT, OWNER_ID
)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER
        self.uptime = None

    async def keep_alive(self):
        """Maintains active connection without spamming"""
        while True:
            try:
                # Just maintain connection - no message needed
                await asyncio.sleep(30)  # 5 minute intervals
                self.LOGGER(__name__).debug("Connection keep-alive check")
            except Exception as e:
                self.LOGGER(__name__).error(f"Keep-alive error: {e}")
                await asyncio.sleep(60)  # Wait before retrying

    async def start(self, use_qr=False, except_ids=None):
        self.LOGGER(__name__).info("🚀 Starting bot initialization...")
        await super().start()
        self.uptime = datetime.now()

        try:
            usr_bot_me = await self.get_me()
            if usr_bot_me is None:
                raise Exception("get_me() returned None. Invalid BOT_TOKEN?")
            self.username = usr_bot_me.username
        except Exception as e:
            self.LOGGER(__name__).error(f"❌ Failed to fetch bot info: {e}")
            self.LOGGER(__name__).info("Check your TG_BOT_TOKEN and ensure bot isn't blocked")
            sys.exit(1)

        # Force Sub Channels Verification
        for idx, channel in enumerate([
            FORCE_SUB_CHANNEL_1, FORCE_SUB_CHANNEL_2,
            FORCE_SUB_CHANNEL_3, FORCE_SUB_CHANNEL_4
        ], 1):
            if channel:
                try:
                    chat = await self.get_chat(channel)
                    link = chat.invite_link or await self.export_chat_invite_link(channel)
                    setattr(self, f"invitelink{'' if idx == 1 else idx}", link)
                except Exception as e:
                    self.LOGGER(__name__).error(f"Force Sub Channel {idx} Error: {e}")
                    self.LOGGER(__name__).info("\nBot Stopped. Join @weebs_support for help")
                    sys.exit(1)

        # DB Channel Verification
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).error(f"DB Channel Error: {e}")
            self.LOGGER(__name__).info("\nBot Stopped. Join @weebs_support for help")
            sys.exit(1)

        self.set_parse_mode(ParseMode.HTML)
        
        # ASCII Art and Startup Log
        self.LOGGER(__name__).info(f"""
╔════════════════════════════╗
║       BOT STARTED          ║
╚════════════════════════════╝
🔹 Username: @{self.username}
🔹 Uptime: {self.uptime}
🔹 Owner: @CulturedTeluguweeb
        """)

        # Web Server Setup with Health Check
        async def health_check(request):
            return web.Response(text="🤖 Bot is running!")

        app = web.Application()
        app.router.add_get("/health", health_check)
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, "0.0.0.0", PORT)
        await site.start()
        self.LOGGER(__name__).info(f"🌐 Web server running on port {PORT}")

        # Start keep-alive task
        asyncio.create_task(self.keep_alive())

        # Notification to owner
        try:
            await self.send_message(
                OWNER_ID,
                f"<b>🚀 Bot Started Successfully!</b>\n"
                f"<b>• Username:</b> @{self.username}\n"
                f"<b>• Uptime:</b> {self.uptime}"
            )
        except Exception as e:
            self.LOGGER(__name__).warning(f"Owner notification failed: {e}")

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("🛑 Bot stopped gracefully")
        try:
            await self.send_message(OWNER_ID, "<b>🛑 Bot Stopped</b>")
        except:
            pass

# Systemd Service Configuration (Save as /etc/systemd/system/ravibot.service)
"""
[Unit]
Description=RaviBot Telegram Service
After=network.target

[Service]
User=root
WorkingDirectory=/path/to/your/bot
ExecStart=/usr/bin/python3 /path/to/your/bot/bot.py
Restart=always
RestartSec=10
Environment="PYTHONUNBUFFERED=1"

[Install]
WantedBy=multi-user.target
"""

if __name__ == "__main__":
    bot = Bot()
    try:
        asyncio.get_event_loop().run_until_complete(bot.start())
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        asyncio.get_event_loop().run_until_complete(bot.stop())
    except Exception as e:
        LOGGER(__name__).error(f"Fatal error: {e}")
        sys.exit(1)
