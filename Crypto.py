from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import sys
import requests


updater = Updater('#####APIKEY######', use_context=True)
dispatcher = updater.dispatcher

#######
def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand what you want :|")

unknown_handler = MessageHandler(Filters.text, unknown)
dispatcher.add_handler(unknown_handler)
########

########
def start(update, context):
    print(update.message)
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm WebCubers bot...")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
########

########
def price(update, context):
    print(update.message.text)
    DigitalMoney = str(update['message']['text']).split(' ')[-1]
    response=requests.get(f'https://api.coinmarketcap.com/v1/ticker/{DigitalMoney}').json()
    context.bot.send_message(chat_id=update.message.chat_id, text=f"{DigitalMoney} price is $ {response[0]['price_usd']}")

start_handler = CommandHandler('price', price)
dispatcher.add_handler(start_handler)
#######
updater.start_polling()