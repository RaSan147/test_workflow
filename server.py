import subprocess

__VERSION = "14-09-2022"

import subprocess
import logging, traceback
import os, threading, time
import requests


os.environ.setdefault("Hoo", "5593984661:AAGnvTbgdfgcujTO8u4di5bxz9-vjxhprP8")

os.environ.setdefault("Loo", "5552810521:AAHkdE9KwGnKIghb6ZdwT-SyhejDV551QGA")




from telegram import __version__ as TG_VER

try:
	from telegram import __version_info__
except ImportError:
	__version_info__ = (0, 0, 0, 0, 0)  
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
	Application,
	CommandHandler,
	ContextTypes,
	ConversationHandler,
	MessageHandler,
	filters
)
from telegram import InputMediaPhoto, InputMediaVideo


application = Application.builder().token(os.environ["Loo"]).build()
logging.basicConfig(
	format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

LINK = 0


def get_ip_info():
	import json
	ip = requests.get("https://api.ipify.org").text
	r = dict(requests.get(f"http://ip-api.com/json/{ip}").json())
	r2 = dict(requests.get(f"https://ipapi.co/{ip}/json").json())
	r.update(r2)
	return json.dumps(r, indent=2)


async def run_server(update):
	# subprocess.call('wget https://git.io/vpn -O openvpn-install.sh'.split())
	subprocess.call('chmod +x openvpn-install.sh'.split())
	subprocess.call('sudo ./openvpn-install.sh'.split())

	await update.message.reply_text("Server is Loaded...")

	subprocess.call('sudo systemctl start openvpn-server@server.service'.split())

	await update.message.reply_text("Server is Started...")
	await update.message.reply_document(open("/root/client.ovpn", "rb"))

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
	"""Cancels and ends the conversation."""
	user = update.message.from_user
	logger.info("User %s canceled the conversation.", user.first_name)
	await update.message.reply_text(
		"Cancelled!", reply_markup=ReplyKeyboardRemove()
	)

	return ConversationHandler.END



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

	await update.message.reply_text("Hi! Drop the code")
	return 0


async def link_job(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
	# bot = context.bot
	# chat_id = update.message.chat_id
	print("working")
	
	the_code = update.message.text
	if the_code.lower() == os.environ["code"]:
		await run_server(update)

	if the_code.lower() == "ip":
		await update.message.reply_text(get_ip_info())

	await update.message.reply_text("Server is down", quote=True)
	
	

def main() -> None:
	"""Run the bot."""
	# Create the Application and pass it your bot's token.
	
	conv_handler = ConversationHandler(
		entry_points =[CommandHandler("asuna", start)],
		states={
			0: [MessageHandler(filters.Regex(".*"), link_job), MessageHandler(filters.ATTACHMENT, photo)],
		},
		fallbacks=[CommandHandler("cancel", cancel)],
	)

	application.add_handler(conv_handler)
	application.run_polling()

if __name__ == "__main__":
	main()


#djeodnfnsjejrosjdJDDJRHWUjdiwksfshsjsjdjDJWOSJFNEJ1837446132946752446*-*-/@#+_(#)_-#)&)#-#)/jxieakdjfjsiiaNdeidjJFEISNH





if __name__ == '__main__':
	run_server()


