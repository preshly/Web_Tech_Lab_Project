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

import sys

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
#from flask_ngrok import run_with_ngrok
import os

from admin_conversation import chancellor_conversation, dean_conversation, vice_chancellor_conversation, registrar_conversation, general_conversation

from courses_conserv import courses_conversation, bachelors_courses_conversation
from courses_conserv import master_courses_conversation, mphil_courses_conversation
from courses_conserv import pgdiploma_courses_conversation, doctoral_courses_conversation

from link_resolver import LinkResolver

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
    "Hi there! This is University chatbot. What can I do for you?",
    "Hi",
    "Hi! This is University chatbot. How can I help you?",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you."
]

# bot = ChatBot("Chatterbot")
trainer = ListTrainer(bot)
trainer.train(conversation)

#training the chatbot with the courses conservation
trainer.train(general_conversation)
trainer.train(chancellor_conversation)
trainer.train(vice_chancellor_conversation)
trainer.train(registrar_conversation)
trainer.train(dean_conversation)
trainer.train(courses_conversation)
trainer.train(bachelors_courses_conversation)
trainer.train(master_courses_conversation)
trainer.train(doctoral_courses_conversation)
trainer.train(mphil_courses_conversation)
trainer.train(pgdiploma_courses_conversation)

static_path = 'university/www.unigoa.ac.in'

app = Flask(__name__, template_folder = static_path,static_folder = static_path, static_url_path = '')

link_resolver = LinkResolver()

#run_with_ngrok(app)

@app.route("/")
def index():
    return render_template("index.html") #starting page

@app.route("/get")
def get_bot_response():
    actResponse = ''
    userText = request.args.get("msg") #get data from input
    response = str(bot.get_response(userText))
    # print(response, file=sys.stderr)
    # if(response[0] == '$'):
    #     resp = response.split("$")
    #     actResponse = getContent(resp[2],resp[2])
    #     app.logger.info(actResponse)
    # else:
    #     actResponse = response
    appendfile = os.listdir('saved_conversations')[-1]
    appendfile = open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('user : '+userText+'\n')
    appendfile.write('bot : '+response+'\n')
    appendfile.close()

    if userText == 'Can you provide more information about Study India Programmme?' \
        or userText == 'Tell me more about Study Japan Programmme' \
        or userText == 'Can you provide more information about the bachelor programme?' \
        or userText == 'Provide more information about the master programme' \
        or userText == 'Tell more things in MPhil' \
        or userText == 'Give more information about doctoral programme' \
        or userText == 'Give more information about PG Diploma':
        resolved_link = link_resolver.resolve_link(response)
        return resolved_link

    return response

# @app.route("/getValue")
# def get_value():
#     value = ''
#     html = request.args.get("html")
#     # incomplete


if __name__ == "__main__":
    app.run()
