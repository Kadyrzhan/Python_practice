import telebot
import config
import json

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def bot_start(message):
    print(message)


if __name__ == '__main__':
    bot.polling(none_stop=True)