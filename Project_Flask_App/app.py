from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "Hi",
    "Hi!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",

]

bot = ChatBot("Chatterbot")
trainer = ListTrainer(bot)
trainer.train(conversation)

from flask_ngrok import run_with_ngrok

static_path = 'university/www.unigoa.ac.in'

app = Flask(__name__, template_folder = static_path,static_folder = static_path, static_url_path = '')
run_with_ngrok(app)

@app.route("/")
def index():
     return render_template("index.html") #to send context to html

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg") #get data from input,we write js  to index.html
     return str(bot.get_response(userText))



#if __name__ == "__main__":
app.run()

