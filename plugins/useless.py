from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS, BOT_STATS_TEXT, USER_REPLY_TEXT, DELETE_DELAY
from datetime import datetime
from helper_func import get_readable_time
import time
import psutil
import asyncio
import logging
import humanize  # For human-readable sizes
from pyrogram.enums import ChatAction
# Admin filter for convenience
admin = filters.user(ADMINS)

@Bot.on_message(filters.command('stats') & admin)
async def stats(bot: Bot, message: Message):
    try:
        # Start with a typing indicator for better UX
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        
        # Get current timestamp
        now = datetime.now()
        
        # --- UPTIME CALCULATION ---
        delta = now - bot.uptime
        uptime = get_readable_time(delta.seconds)
        
        # --- PING TEST WITH PROGRESSIVE ANIMATION ---
        ping_steps = ["🏓 Pinging...", "🏓 Pinging....", "🏓 Pinging....."]
        ping_msg = await message.reply(ping_steps[0])
        
        # Animate ping test
        for step in ping_steps[1:]:
            await asyncio.sleep(0.3)
            await ping_msg.edit(step)
        
        start_time = time.perf_counter()
        await bot.get_me()  # Lightweight API call for accurate ping
        end_time = time.perf_counter()
        ping = round((end_time - start_time) * 1000, 2)  # ms with 2 decimal places
        
        # --- SYSTEM METRICS ---
        mem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        disk = psutil.disk_usage('/')
        
        # --- BOT-SPECIFIC METRICS ---
        active_tasks = len([t for t in asyncio.all_tasks() if not t.done()])
        bot_users = await full_userbase()
        
        # --- FORMATTED OUTPUT ---
        stats_text = f"""
<b>🤖 BOT STATISTICS</b>
━━━━━━━━━━━━━━
<b>⏱️ Uptime:</b> <code>{uptime}</code>
<b>📶 Ping:</b> <code>{ping} ms</code>

<b>💻 SYSTEM RESOURCES</b>
━━━━━━━━━━━━━━
<b>🧠 Memory:</b> <code>{mem.percent}%</code> ({humanize.naturalsize(mem.used)}/{humanize.naturalsize(mem.total)})
<b>🔀 Swap:</b> <code>{swap.percent}%</code> ({humanize.naturalsize(swap.used)}/{humanize.naturalsize(swap.total)})
<b>💾 Disk:</b> <code>{disk.percent}%</code> ({humanize.naturalsize(disk.used)}/{humanize.naturalsize(disk.total)})
<b>🔥 CPU:</b> <code>{psutil.cpu_percent(interval=0.5)}%</code> ({psutil.cpu_count()} cores)

<b>📊 BOT METRICS</b>
━━━━━━━━━━━━━━
<b>👥 Users:</b> <code>{len(bot_users)}</code>
<b>🔧 Active Tasks:</b> <code>{active_tasks}</code>
<b>🔄 Last Update:</b> <code>{now.strftime('%Y-%m-%d %H:%M:%S')}</code>
"""
        # --- SEND FINAL RESULT ---
        await ping_msg.edit(stats_text, disable_web_page_preview=True)
        
        # --- AUTO-CLEANUP ---
        if DELETE_DELAY > 0:
            await asyncio.sleep(DELETE_DELAY)
            await ping_msg.delete()
            
    except Exception as e:
        logger.error(f"Stats command failed: {e}")
        await message.reply("⚠️ Failed to gather statistics. Please try again later.")

@Bot.on_message(filters.private & filters.incoming)
async def useless(_, message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)
