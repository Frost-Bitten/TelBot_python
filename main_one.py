from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token='1048309903:AAFvA1djwosUF-MnZLR39G6LweAQl80c328', use_context='true')
dispatcher = updater.dispatcher
# start_handler = CommandHandler('start', start)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please kiss me! 💋 💋 💋")


def end(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SO FUCK OFF !!! 🖕🏻 🖕🏻 🖕🏻")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


start_handler = CommandHandler('start', start)
end_handler = CommandHandler('end', end)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(end_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()

