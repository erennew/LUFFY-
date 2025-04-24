from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT, DELETE_DELAY
from datetime import datetime
from helper_func import get_readable_time
import time
import psutil
import asyncio

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))  # Only admins allowed to use /stats
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    uptime = get_readable_time(delta.seconds)

    start_time = time.time()
    ping_response = await message.reply("Pinging...")  # Bot replies with "Pinging..."
    end_time = time.time()
    ping = round((end_time - start_time) * 1000)  # Calculate ping in milliseconds

    # Memory usage
    memory_info = psutil.virtual_memory()
    memory_usage = f"{memory_info.percent}%"

    # CPU usage
    cpu_usage = f"{psutil.cpu_percent(interval=1)}%"

    # Formatting the stats text
    stats_text = f"""
    <b>Bot Stats:</b>
    <b>Uptime:</b> {uptime}
    <b>Ping:</b> {ping}ms
    <b>Memory Usage:</b> {memory_usage}
    <b>CPU Usage:</b> {cpu_usage}
    <b>Last Fetched:</b> {now.strftime('%Y-%m-%d %H:%M:%S')}
    """

    # Send the stats message
    await ping_response.edit(stats_text)

    # Auto-delete the message after the configured DELETE_DELAY time
    

    await asyncio.sleep(DELETE_DELAY)
    await ping_response.delete()


@Bot.on_message(filters.private & filters.incoming)
async def useless(_, message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
