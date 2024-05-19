import asyncio
import logging
import schedule
import threading
import telebot
import time
import json
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from aiogram.dispatcher.router import Router

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
        await StudentData().add_data_to_json(users_name, join_date)


@dp.message(Command('start'))
async def on_start(message: types.Message):
    # приветствие пользователя

    await message.answer(f"бот запущен ID группы, {message.chat.id}")
    chat_id = message.chat_id

@dp.message(Command('update'))
async def on_update(message):
    StudentData().update_json()
    await bot.send_message(message.chat.id, f"Данные обновлены!")


with open('data_tests/road_map.json', 'r') as file:
    road_map = json.load(file)

with open('data_tests/members.json', 'r') as file:
    members = json.load(file)


async def send_messages(member, message):
    await bot.send_message(member['name'], message)


@router.message(Command('progress'))
async def personal_message_for_all_members():
    StudentData().update_json()

    for member in members:

        prev_progress = str(int(member['current_progress']) - 1)
        if prev_progress in road_map:
            await send_messages(member, 'v предыдущий этап: ' + road_map[prev_progress])
        else:
            print(f"Ключ {prev_progress} не существует в словаре road_map.")

        await send_messages(member, '> текущий этап: ' + road_map.get(member['current_progress'], "Progress not found"))

        next_progress = str(int(member['current_progress']) + 1)
        if next_progress in road_map:
            await send_messages(member, 'x следующий этап: ' + road_map[next_progress])
        else:
            print(f"Ключ {next_progress} не существует в словаре road_map.")


# schedule.every().day.at("09:48").do(personal_message_for_all_members)


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


thread = threading.Thread(target=run_schedule)
thread.start()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
