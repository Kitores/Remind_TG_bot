from aiogram import Bot
from time import sleep
async def send_message_cron(bot: Bot):
    for i in range(10):
        sleep(5)
        await bot.send_message("id", "hello")

async def send_message_time(bot: Bot):
    for i in range(10):
        sleep(5)
        await  bot.send_message("id", "hi")
