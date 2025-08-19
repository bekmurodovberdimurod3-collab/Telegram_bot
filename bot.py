import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Tokenni Railway dagi Environment Variables ichidan olamiz
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'vote'])
def vote(message):
    markup = InlineKeyboardMarkup()

    # Siz bergan link bilan tugma
    btn = InlineKeyboardButton(
        "🗳 Ovoz berish",
        url="https://openbudget.uz/boards/initiatives/initiative/52/7f50d29b-0efa-46d0-81c1-1fee828b25d2"
    )
    markup.add(btn)

    bot.send_message(
        message.chat.id,
        "Ovoz berish uchun quyidagi tugmani bosing 👇",
        reply_markup=markup
    )

print("✅ Ovoz berish bot ishga tushdi...")
bot.infinity_polling()
