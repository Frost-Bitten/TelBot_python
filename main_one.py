from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token='1048309903:AAFvA1djwosUF-MnZLR39G6LweAQl80c328', use_context='true')
dispatcher = updater.dispatcher
# start_handler = CommandHandler('start', start)
def startMe(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', startMe)
dispatcher.add_handler(start_handler)

updater.start_polling()

