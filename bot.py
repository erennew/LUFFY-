import asyncio
import sys
from aiohttp import web
from pyrogram import Client
from pyrogram.enums import ParseMode
from datetime import datetime
import pyromod.listen

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
        self.restart_count = 0
        self.uptime = None

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
            self.LOGGER(__name__).error(f"❌ Failed to fetch bot info using get_me(): {e}")
            sys.exit()

        # Notify owner
        try:
            await self.send_message(
                OWNER_ID,
                text=(
                    f"<b><blockquote>🤖 Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ ✅\n\n"
                    f"🔁 Restart Count: <code>{self.restart_count}</code></blockquote></b>"
                )
            )
        except Exception as e:
            self.LOGGER(__name__).warning(f"Couldn't send restart message: {e}")

        # Force Sub Channel Links
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
                    self.LOGGER(__name__).warning(f"Force Sub Channel {idx} Error: {e}")
                    sys.exit()

        # DB Channel Check
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(f"Check DB Channel Error: {e}")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info("✅ Bot started successfully.")

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("🛑 Bot stopped gracefully.")

    async def web_server(self):
        async def index(request):
            return web.Response(text="✅ Bot is Alive")
        app = web.Application()
        app.router.add_get("/", index)
        return app

def run_bot():
    bot = Bot()
    loop = asyncio.get_event_loop()

    async def _main():
        while True:
            try:
                bot.restart_count += 1
                await bot.start()

                # Web server (Koyeb ping)
                app = await bot.web_server()
                runner = web.AppRunner(app)
                await runner.setup()
                site = web.TCPSite(runner, "0.0.0.0", PORT)
                await site.start()

                bot.LOGGER(__name__).info(f"🌐 Web server started on port {PORT}")
                bot.LOGGER(__name__).info(f"🔁 Restart Count: {bot.restart_count}")

                await asyncio.Event().wait()  # Keep running

            except Exception as e:
                bot.LOGGER(__name__).error(f"🔥 Bot crashed: {e}", exc_info=True)
                await bot.stop()
                await asyncio.sleep(5)  # Wait before restart

    try:
        loop.run_until_complete(_main())
    except KeyboardInterrupt:
        loop.run_until_complete(bot.stop())
        bot.LOGGER(__name__).info("⛔ Stopped by user.")


