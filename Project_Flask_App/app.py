from flask import Flask, render_template, request
import os
from chatbot import Nltk_Convo

try:
	os.remove("db.sqlite3")
	print("Old database removed. Training new database")
except:
	print('No database found. Creating new database.')

bot = Nltk_Convo()
# bot.chat_response('hi') #to remove extra time needed for bot response for first user message.

files = os.listdir('saved_conversations')
files = [int(f) for f in files]
filenumber= max(files)
filenumber=filenumber+1

file= open('saved_conversations/'+str(filenumber),"w+")
file.write('bot : Hello Im university bot. How can I help you?\n')
file.close()

##Flask app

static_path = 'university/www.unigoa.ac.in'

app = Flask(__name__, template_folder = static_path,static_folder = static_path, static_url_path = '')

@app.route("/")
def index():
    return render_template("index.html") #starting page

@app.route("/get")
def get_bot_response():
    response = ''
    userText = request.args.get("msg") #get data from input
    print("user text "+userText)
    # response = str(bot.get_response(userText))
    response = bot.chat_response(userText)

    # appendfile = os.listdir('saved_conversations')[-1]

    appendfile = open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('user : '+userText+'\n')
    appendfile.write('bot : '+response+'\n')
    appendfile.close()

    return response

if __name__ == "__main__":
    app.run()
