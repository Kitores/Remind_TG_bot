import asyncio, logging
import aioschedule
from aiogram import Bot, Dispatcher, types
from aiogram.loggers import middlewares
from aiogram.filters.command import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from Scripts.handlers import apsched
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6442408002:AAFAu3GRCZVcVrie58j6hmcbqOemHz8_dzY")
# Диспетчер
dp = Dispatcher()
User_ID = 874999696
txt = "fnjf;jlnalnf"
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
scheduler.add_job(apsched.send_message_time, trigger='date', run_date=datetime.now() + timedelta(seconds=10),
                  kwargs={'bot': bot})
scheduler.add_job(apsched.send_message_cron, trigger='cron', hour=8, minute=0,  kwargs={'bot' : bot})

# dp.middleware.setup(middlewares)
# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    scheduler.start()
    chat_ID = message.from_user.id
    await message.answer(f"Hello! Your id = {chat_ID}")

@dp.message(Command("ret"))
async def remind(messaege: types.Message):
    remi(User_ID)
    await bot.send_message(User_ID, "sfsfsf")

# async def send_message(message: txt, hour:int, minute: int):
#     try:
#         await bot.send_message(chat_id=User_ID, text=txt)
#     except Exception as e:
#         print(e)

# async def send_scheduled_messages():
#
#
#     scheduler.start()
#     await asyncio.sleep(24 * 60 * 60)
#     scheduler.shutdown()
# async def scheduler():
#     aioschedule.every().day.at("11:45").do(send_message(txt,12,32))
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)

# async def on_startup(dp):
#     asyncio.create_task(scheduler())

#Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    # loop.create_task(send_scheduled_messages())
    # executor.start_polling(dp, loop=loop)
