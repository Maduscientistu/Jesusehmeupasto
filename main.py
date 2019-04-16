from telegram.ext import Updater, CommandHandler
import os

TELEGRAM_KEY = os.environ.get("BOT_KEY")

def start(update, context):
	context.bot.send_message("Hello, i don't like your face. Don't talk to me, ugly people don't belong to this world. ;P")
	
updater = Updater(token=TELEGRAM_KEY, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()