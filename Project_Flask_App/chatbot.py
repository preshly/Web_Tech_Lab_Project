# import os

# from flask import Flask, render_template, request, jsonify, Response, request
# # from chatterbot import chatterbot
# # from chatterbot.trainers import ChatterBotCorpusTrainer

# static_path = 'university/www.unigoa.ac.in'

# app = Flask(__name__, template_folder = static_path,static_folder = static_path, static_url_path = '')

# @app.route('/')
# def homepage():
#     return render_template('index.html')
# if __name__ == '__main__':
#     app.run()


from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from flask_ngrok import run_with_ngrok
import os

try:
	os.remove("db.sqlite3")
	print("Old database removed. Training new database")
except:
	print('No database found. Creating new database.')

filenumber=int(os.listdir('saved_conversations')[-1])
filenumber=filenumber+1
file= open('saved_conversations/'+str(filenumber),"w+")
file.write('bot : Hello Im university bot. How can I help you?\n')
file.close()

bot = ChatBot(
    'Chatterbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

trainer = ListTrainer(bot)

conversation = [
    "Hello",
    "Hi there! What can I do for you?",
    "Hi",
    "Hi! How can I help you?",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you."
]

demo = [
    "hello mca",
    "welcome to mca",

]

# bot = ChatBot("Chatterbot")
trainer = ListTrainer(bot)
trainer.train(conversation)
trainer.train(demo)

static_path = 'university/www.unigoa.ac.in'

app = Flask(__name__, template_folder = static_path,static_folder = static_path, static_url_path = '')
run_with_ngrok(app)

@app.route("/")
def index():
    return render_template("index.html") #to send context to html

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg") #get data from input,we write js  to index.html
    response = str(bot.get_response(userText))
    appendfile=os.listdir('saved_conversations')[-1]
    appendfile= open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('user : '+userText+'\n')
    appendfile.write('bot : '+response+'\n')
    appendfile.close()

    return response



if __name__ == "__main__":
    app.run()
