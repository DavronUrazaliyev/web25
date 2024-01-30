from flask import Flask
import telegram
# Create the application instance
app = Flask(__name__)

TOKEN ='6440042136:AAGp50G4rRElB42wkDg7DlM91-opDBQwjhc'
bot = telegram.Bot(TOKEN)
chat_id = '5271463532'

# route for index page
@app.route('/', methods=['POST'])
def index():
    print('index page')
    bot.send_message(chat_id=chat_id, text='Hello World!!!')
    return 'index page'
