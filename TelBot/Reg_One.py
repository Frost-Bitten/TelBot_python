from telegram.ext import MessageHandler, CommandHandler, Updater
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

up = Updater(token='1048309903:AAFvA1djwosUF-MnZLR39G6LweAQl80c328', use_context='true')
dis = up.dispatcher
studentList = list()


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello ! please use this format for registering :\n"
                                                                    "/reg Name FamilyName")


def reg(update, context):
    studentList.append(context.args)


def result(update, context):
    if studentList == []:
        context.bot.send_message(chat_id=update.effective_chat.id, text="List is empty !")
    else:
        resStr = str()
        for i in studentList:
            for j in i:
                resStr += j+" "
            resStr += "\n"
        context.bot.send_message(chat_id=update.effective_chat.id, text=resStr)


def clear(update, context):
    studentList.clear()
    context.bot.send_message(chat_id=update.effective_chat.id, text="List successfully cleared !")


start_handler = CommandHandler('start', start)
reg_handler = CommandHandler('reg', reg)
result_handler = CommandHandler('result', result)
clear_handler = CommandHandler('clear', clear)
dis.add_handler(clear_handler)
dis.add_handler(result_handler)
dis.add_handler(start_handler)
dis.add_handler(reg_handler)

up.start_polling()
