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
import ephem
import logging



from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(update, bot):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def astro_user(update, bot):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    text = 'Вызван /planet'
    print(text)
    t = update.message.text
    planet_name = str(update.message.text.split(' ')[1]).capitalize()
    print(planet_name)
    if planet_name in planets:
        planet = getattr(ephem, planet_name)
        pl = planet('2020')
        print(ephem.constellation(pl))
    else:
        update.message.reply_text('Имя планеты введено неправильно. После "/planet " введите английское имя планеты.')
        print('Имя планеты введено неправильно. После "/planet " введите английское имя планеты.')
    update.message.reply_text(text)

def talk_to_me(update, bot):
    print('Message arrived')
    user_text = update.message.text
    print("!!!!!!")
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater("872877235:AAFkR-nauiGvoZvkUMBp_hoxBngLCnSxqP4", request_kwargs=PROXY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", astro_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
