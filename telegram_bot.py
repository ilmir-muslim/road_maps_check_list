from datetime import datetime
import telebot
import TOKEN
from add_new_member_to_json import add_data_to_json

TOKEN = TOKEN.TOKEN
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Категорически приветствую, бот запущен!')


@bot.message_handler(content_types=['new_chat_members'])
async def on_new_chat_members(update, context):
    new_members = update.message.new_chat_members
    for member in new_members:
        await update.message.reply_text(f"Добро пожаловать, {member.first_name}!")
        join_date = datetime.utcfromtimestamp(member.date).strftime('%d-%m-%Y')
        users_name = member.first_name
        await add_data_to_json(users_name, join_date)


bot.infinity_polling(none_stop=True)
