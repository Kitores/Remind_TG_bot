from aiogram import Bot
from time import sleep
async def send_message_cron(bot: Bot):
    for i in range(10):
        sleep(5)
        await bot.send_message(874999696, "kjvnkjndl")

async def send_message_time(bot: Bot):
    for i in range(10):
        sleep(5)
        await  bot.send_message(874999696, "41412421")
