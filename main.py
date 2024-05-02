from datetime import datetime

import telebot
import manipulate_with_json as manipulate

TOKEN = 'BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['new_chat_members'])
async def on_new_chat_members(update):
    # добавление нового участника

        await update.message.reply_text(f"У нас новенький - , {update.first_name}, привет 🙂!")
        join_date = datetime.utcfromtimestamp(update.date).strftime('%d-%m-%Y')
        users_name = update.first_name
        await manipulate.add_data_to_json(users_name, join_date)


bot.infinity_polling(none_stop=True)
