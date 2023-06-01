import requests
import random
import telegram
from telegram.ext import Updater, CommandHandler

# Define the API endpoint and parameters
API_ENDPOINT = "http://quotes.rest/qod.json"
API_PARAMS = {
    "category": "inspire",
    "language": "en"
}

# Define the Telegram bot token and chat ID
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"

# Define the Telegram bot instance
bot = telegram.Bot(token=BOT_TOKEN)

# Define the function to fetch a quote from the API
def get_quote():
    response = requests.get(API_ENDPOINT, params=API_PARAMS)
    data = response.json()
    quote = data["contents"]["quotes"][0]["quote"]
    return quote

# Define the function to send a quote to a Telegram user
def send_quote(bot, update):
    chat_id = update.message.chat_id
    quote = get_quote()
    bot.send_message(chat_id=chat_id, text=quote)

# Set up the Telegram bot updater and command handler
updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("quote", send_quote))

# Start the Telegram bot
updater.start_polling()

# Keep the bot running
updater.idNote that in order to use this program, you will need to replace the placeholders for the bot token and chat ID with your own values. You will also need to install the python-telegram-bot library using pip:
