import telebot
import TOKEN
TOKEN = TOKEN.TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Категорически приветствую, бот запущен!')

bot.polling(none_stop=True)