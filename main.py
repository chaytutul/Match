import telebot
from telebot import types

from config import *

print("Active")
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    print('Hello World')
    print()


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call): ...


@bot.message_handler(content_types=["text"])
def handler_text(message): ...


bot.polling(none_stop=True, interval=0, timeout=20)