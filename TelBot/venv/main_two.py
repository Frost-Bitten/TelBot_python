from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
updater = Updater(token='1048309903:AAFvA1djwosUF-MnZLR39G6LweAQl80c328', use_context='true')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the second test")


def cap(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text.upper())
    print(type(update.effective_chat.id))
    print(type(update.message.text))

start_handler = CommandHandler('start', start)
cap_handler = MessageHandler(Filters.text, cap)

dispatcher.add_handler(cap_handler)
dispatcher.add_handler(start_handler)

updater.start_polling()


