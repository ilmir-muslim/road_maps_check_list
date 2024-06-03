import asyncio
import logging
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.filters.command import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from studentdata import StudentData

logging.basicConfig(level=logging.INFO)
API_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()


@dp.message(F.new_chat_members)
async def on_new_chat_members(message):
    # добавление новых участников
    for user in message.new_chat_members:
        await bot.send_message(message.chat.id, f"У нас новенький - {user.full_name}, привет 🙂!")
        join_date = datetime.utcfromtimestamp(message.date.timestamp()).strftime('%d.%m.%Y')
        users_name = user.full_name
        user_id = user.id
        await StudentData().add_data_to_db(user_id, users_name, join_date)


@dp.message(Command('start'))
async def on_start(message: types.Message):
    # приветствие пользователя

    await message.answer(f"бот запущен,приветствую!")


async def send_messages(member, text):
    await bot.send_message(member, text)

@dp.message(F,text)
#здесь будет отправка дейлика

@dp.message(F.text)
async def personal_message_for_all_members(message: types.Message):
    members = StudentData().get_user_id()

    for user_id in members:
        current_progress = StudentData().get_current_progress(user_id)

        if current_progress > 1:
            previous_stage = StudentData().previous_stage(current_progress)
        else:
            previous_stage = 'Начало обучения'

        studying_stage = StudentData().get_studying_stage(user_id)
        next_stage = StudentData().next_stage(current_progress)

        message_for_send = (f"--- предыдущий этап: {previous_stage} \n\n"
                            f" >>> Текущий этап: {studying_stage} \n\n"
                            f"--- следующий этап: {next_stage} \n")
        try:
            await send_messages(user_id, message_for_send)
        except Exception as e:
            print(e)


@dp.message(Command('addme'))
async def addme(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    try:
        await StudentData().add_data_to_db(user_id, user_name, '01.01.1900')
    except Exception as e:
        print(e)


# schedule.every().day.at("21:02").do(personal_message_for_all_members)


# async def run_schedule():
#     while True:
#         schedule.run_pending()
#         time.sleep(1)


# thread = threading.Thread(target=run_schedule)
# thread.start()


async def main():
    await dp.start_polling(bot)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(personal_message_for_all_members, "interval", seconds=10,
                      start_date='2000-01-01 00:00:00')
    scheduler.start()
    await asyncio.sleep(float('inf'))


if __name__ == "__main__":
    asyncio.run(main())


@dp.message(Command('test'))
async def test():
    await personal_message_for_all_members()
