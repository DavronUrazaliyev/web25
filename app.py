from flask import Flask, request
import telegram  


app = Flask(__name__)

TOKEN ='6440042136:AAGp50G4rRElB42wkDg7DlM91-opDBQwjhc'
bot = telegram.Bot(TOKEN)
chat_id = '5271463532'
URL = 'https://davron17.pythonanywhere.com/'

bot.delete_webhook()
bot.setWebhook(URL)

@app.route('/', methods=['POST'])
def index():
    print('index page')
    
    data=request.json()
    print(data)
    chat_id = data.chat_id
    text = data.text
    bot.send_message(chat_id=chat_id, text=text)
    return 'bot ishlaayapti'
    
