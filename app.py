from flask import Flask, request
import telegram  
from telegram import Update
from telegram.ext import CallbackContext, MessageHandler, Filters, Updater



app = Flask(__name__)

TOKEN ='6440042136:AAGp50G4rRElB42wkDg7DlM91-opDBQwjhc'
bot = telegram.Bot(TOKEN)
chat_id = '5271463532'
URL = 'https://davron17.pythonanywhere.com/'


bot.delete_webhook()
bot.setWebhook(URL)
# route for index page
@app.route('/', methods=['POST'])
def index(update: Update, context: CallbackContext):
    print('index page')
    chat_id = update.message.chat_id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=text)
    return 'bot ishlaayapti'
    
    
    

if __name__ == "__main__":
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    app.run(debug=True)
    updater.idle()
print(bot.get_webhook_info())