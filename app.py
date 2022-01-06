from telegram.ext import updater , dispatcher
from telegram.ext import commandhandler , MessageHandler,filters
import os
TOKEN = os.environ.get("API_KEY")

def start(updater,context):
    yourname = updater.message.chat.first_name


    msg = "hi"+yourname+"!welcome to telebot"
    context.bot.send_message(updater.message.chat.id,msg)

def echo_msg(upadter,context):
    context.bot.send_message(updater.message.chat.id,upadter.message.text)

def error(updater,context):
    context.bot.send_message(updater.message.chat.id,"oop! error occured")
    context.bot.send_photo(updater.message.chat.id,"https://images.app.goo.gl/4XSBzaL38YcJbaec9")


def details(updater,context):
    context.bot.send_message(updater.message.chat.id,updater.message)
def main():
    Updater = updater(token = TOKEN )

    dp = updater.dispatcher

    dp.add_hander(commandhandler("start",start))
    dp.add_hander(commandhandler(filters.text,echo_msg))
    dp.add_hander(commandhandler("update",details))

    dp.add_error_handler(error)
#set up webhook
    updater.start_webhook(listen = "0.0.0.0",port = os.envon.get("PORT",443) ,
                                url_path = TOKEN,
                                webhook_url="https://myth-telebot-app.heroku.com"+TOKEN)
    Updater.idle()

if __name__ == '__main__':
    main()

