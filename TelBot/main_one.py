from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token='1048309903:AAFvA1djwosUF-MnZLR39G6LweAQl80c328', use_context='true')
dispatcher = updater.dispatcher
studentList = list()


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please kiss me! 💋 💋 💋")


def end(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SO FUCK OFF !!! 🖕🏻 🖕🏻 🖕🏻")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    # print(update.message.text)
    # name = str(update.effective_chat.id)
    # outFile = open(name+'.txt', "a")
    # outFile.write(update.message.text)
    # outFile.write('\n')


def cap(update, context):
    print(context.args)
    print(type(context.args))
    text_out = " ".join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_out)


def reg(update, context):
    studentList.append(context.args)


def out(update, context):
    outPut = str()
    for i in studentList:
         outPut += i[0]+" "+i[1]+"\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=outPut)


start_handler = CommandHandler('start', start)
end_handler = CommandHandler('end', end)
echo_handler = MessageHandler(Filters.text, echo)
cap_handler = CommandHandler('cap', cap)
reg_handler = CommandHandler('reg', reg)
out_handler = CommandHandler('result', out)
dispatcher.add_handler(reg_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(end_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(cap_handler)
dispatcher.add_handler(out_handler)
updater.start_polling()

