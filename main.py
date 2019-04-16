from telegram.ext import Updater, CommandHandler
import requests
import os

port = os.environ.get("PORT", 5000)
os.system('python -m http.server ' + port + ' &')


TELEGRAM_KEY = os.environ.get("BOT_KEY")
updater = Updater(token=TELEGRAM_KEY, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text="Hello, i don't like your face. Don't talk to me, ugly people don't belong to this world. ;P")

def traps(update, context):
	context.bot.send_message(chat_id=update.message.chat_id, text="There's no greater ire,\n no greater fire\n than the one burning in my soul. \n Why make it so so vile\n Man of little faith \n Traps are all my style\n My purpose and my fate.")

def sendcatpics(update, context):
	print("vc ta bein?")
	fotoCat = requests.get("https://api.thecatapi.com/v1/images/search")
	if fotoCat.response_code == 200:
		fotoURL = fotoCat.json()[0]['url']
		print(fotoURL)
		context.bot.send_photo(chat_id=update.message.chat_id, photo=fotoURL)
	else:
		traps(update, context)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('notgay', traps))
dispatcher.add_handler(CommandHandler('cat', sendcatpics))

updater.start_polling()