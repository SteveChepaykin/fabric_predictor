import telebot
import config
import requests
import os
from telebot import types

bot = telebot.TeleBot(config.BOTTOKEN)

neural_host = os.environ.get('NEURAL_HOST', 'service_neural')

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    weatherb = types.KeyboardButton('Получить информацию')
    markup.add(weatherb)
    bot.send_message(message.chat.id, "Hi, {0.first_name}".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['forecast'])
def welcome(message):
    resp = requests.get(f"http://{neural_host}:5050/forecast").json()
    if resp["status"] == "OK":
        bot.send_message(message.chat.id, 'Все ок')
    elif resp["status"] == "BAD":
        bot.send_message(message.chat.id, 'Что то не ок')
    else: bot.send_message(message.chat.id, 'Нет достаточных данных для прогноза.')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    typeb = types.KeyboardButton('Получить информацию')
    markup.add(typeb) 
    bot.send_message(message.chat.id, '''Чтобы получить данные по производственной линии, выберите 
                     команду /forecast или нажмите кнопку ниже.''', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def reply(message):
    if message.chat.type == 'private':
        if message.text == 'Получить информацию':
            resp = requests.get(f"http://{neural_host}:5050/forecast").json()
            if resp["status"] == "OK":
                bot.send_message(message.chat.id, 'Все ок')
            elif resp["status"] == "BAD":
                bot.send_message(message.chat.id, 'Что то не ок')
            else: bot.send_message(message.chat.id, 'Нет достаточных данных для прогноза.')

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            typeb = types.KeyboardButton('Получить информацию')
            markup.add(typeb) 
            bot.send_message(message.chat.id, '''Чтобы получить данные по производственной линии, выберите команду /forecast 
                             или нажмите кнопку ниже.''', reply_markup=markup)

        elif message.text != '':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            typeb = types.KeyboardButton('Получить информацию')
            markup.add(typeb) 
            bot.send_message(message.chat.id, '''Не знаю что на это ответить.\nЧтобы получить данные по производственной линии, 
                             выберите команду /forecast или нажмите кнопку ниже.''', reply_markup=markup)

bot.polling(non_stop=True)