import telebot
import TOKEN
TOKEN = TOKEN.TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Категорически приветствую, бот запущен!')


def on_new_chat_members(update):
    new_members = update.message.new_chat_members
    for member in new_members:
        update.message.reply_text(f"Добро пожаловать, {member.first_name}!")

bot.polling(none_stop=True)