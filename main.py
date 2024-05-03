from datetime import datetime
import telebot
from studentdata import StudentData
import schedule
import os

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['new_chat_members'])
async def on_new_chat_members(update):
    # добавление нового участника

    await update.message.reply_text(f"У нас новенький - , {update.first_name}, привет 🙂!")
    join_date = datetime.utcfromtimestamp(update.date).strftime('%d-%m-%Y')
    users_name = update.first_name
    await StudentData().add_data_to_json(users_name, join_date)


@bot.message_handler(commands=['start'])
def on_start(message):
    # приветствие пользователя

    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!")


@bot.message_handler(commands=['update'])
def on_update(message):
    StudentData().update_json()
    bot.send_message(message.chat.id, f"Данные обновлены!")


bot.infinity_polling(none_stop=True)
