from flask import Flask, request
import telegram
from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters, Updater

app = Flask(__name__)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6440042136:AAGp50G4rRElB42wkDg7DlM91-opDBQwjhc'
bot = telegram.Bot(token=TOKEN)

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=text)  # Fix the syntax error here

@app.route('/', methods=['POST'])
def index():
    return 'Hello from Flask!'

if __name__ == "__main__":
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    app.run(debug=True)
    updater.idle()
