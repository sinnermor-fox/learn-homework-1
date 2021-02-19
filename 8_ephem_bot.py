"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import datetime
import logging

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    print('Обрабатываю текст')
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def planet_comand(update, context):
    print('Вызван обработчик команды /planet')
    planet_name = update.message.text.split("/planet ")[1]
    today = datetime.date.today().strftime('%Y/%m/%d')
    planet = None
    if planet_name == "mars":
        planet = ephem.Mars(today)
    elif planet_name == "venus":
        planet = ephem.Venus(today)
    elif planet_name == "mercury":
        planet = ephem.Mercury(today)
    elif planet_name == "earth":
        planet = ephem.Earth(today)
    elif planet_name == "jupiter":
        planet = ephem.Jupiter(today)
    elif planet_name == "saturn":
        planet = ephem.Saturn(today)
    elif planet_name == "uranus":
        planet = ephem.Uranus(today)
    elif planet_name == "neptune":
        planet = ephem.Neptune(today)
    elif planet_name == "pluto":
        planet = ephem.Pluto(today)
    constellation = ephem.constellation(planet)
    update.message.reply_text(str(constellation))


def main():
    mybot = Updater("972243089:AAEcyhhM1O94DeIjrgYHSXUDF5BhXkoy5OU", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_comand))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
