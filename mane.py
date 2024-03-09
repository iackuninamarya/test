import datetime
import random

import telebot
API_TOKEN = '7189894348:AAGwjwOaYLHQr5yykoJLIEooPp0GfGq1QRc'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = ('Привет, я бот для выбора фильма на вечер!\n\n'
            ' Список команд:\n'
            '/get_date - сегодняшняя дата\n'
            '/get_film - получить фильм на вечер')
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['get_date'])
def get_date(message: telebot.types.Message):
    current_date = datetime.datetime.now()
    text = f'Сегодняшняя дата: {current_date.date()}'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["get_film"])
def get_film(message: telebot.types.Message):
    with open("film.txt", "r", encoding="utf-8") as file:
        films = file.read().split("\n")
    film = random.choice(films)
    bot.send_message(message.chat.id, text=f'Сегодня вечером можно посмотреть "{film}"')


@bot.message_handler(func= lambda _: True)
def unknown_command(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Неизвестная команда")


bot.infinity_polling()
