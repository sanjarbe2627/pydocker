import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(
    filename="log.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S"
)


def start(update, context):
    user_data = update.message.from_user
    context.bot.send_message(user_data.id, "Hello.........")


def message_handler(update, context):
    user_data = update.message.from_user
    context.bot.send_message(user_data.id, "Hello.........")


def main():
    updater = Updater("5934228964:AAF2QWvrQM-4egz6EhKprhe88msExQ3PWyQ")

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

    updater.start_polling()
    updater.idle()


main()
