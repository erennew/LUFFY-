import asyncio
from bot import Bot

if __name__ == "__main__":
    bot = Bot()
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(bot.start())
        loop.run_forever()
    except KeyboardInterrupt:
        loop.run_until_complete(bot.stop())
    except Exception as e:
        print(f"Fatal error: {e}")
        loop.run_until_complete(bot.stop())
