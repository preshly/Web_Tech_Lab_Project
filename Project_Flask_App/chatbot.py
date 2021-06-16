
#import necessary libraries
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#import conversations

# from greetings_convers import general_conversation

from admin_conversation import chancellor_conversation, dean_conversation, \
    vice_chancellor_conversation, registrar_conversation, general_conversation, \
    finance_officer_conversation

from greetings_convers import greetings_conversation
# general_course_conversation
from courses_conserv import courses_conversation, bachelors_courses_conversation,\
    master_courses_conversation, mphil_courses_conversation, pgdiploma_courses_conversation, \
    doctoral_courses_conversation, general_course_conversation

from department_convers import department_conversation
from examination_conv import apply_for_conversations, convocation_conversations
from admission_conv import admission_notices_converstion

from contact_conv import contact_conversations,email_conversations

from college_convo import genral_college_conversation, general_edu_institution_convo, \
    professional_edu_institution_convo, recognised_edu_institution_convo

from academic_matter_conv import eligibility_conversations,migration_conversations,transcripts_conversations

from hostel_conves import hostel_conversation

#importing class to convert text to links
#from link_resolver import LinkResolver

try:
	os.remove("db.sqlite3")
	print("Old database removed. Training new database")
except:
	print('No database found. Creating new database.')


# filenumber=int(os.listdir('saved_conversations')[-1])
# filenumber=filenumber+1

files = os.listdir('saved_conversations')
files = [int(f) for f in files]
filenumber= max(files)
filenumber=filenumber+1

file= open('saved_conversations/'+str(filenumber),"w+")
file.write('bot : Hello Im university bot. How can I help you?\n')
file.close()

bot = ChatBot(
    'Goa_University_Chatbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)

#Training the chatbot

trainer = ListTrainer(bot)

#training the chatbot with the greetings_conversation
trainer.train(greetings_conversation)

trainer.train(genral_college_conversation)
trainer.train(general_edu_institution_convo)
trainer.train(professional_edu_institution_convo)
trainer.train(recognised_edu_institution_convo)

trainer.train(general_conversation)
trainer.train(general_course_conversation)
trainer.train(chancellor_conversation)
trainer.train(vice_chancellor_conversation)
trainer.train(registrar_conversation)
trainer.train(dean_conversation)
trainer.train(finance_officer_conversation)

#training the chatbot with the courses conservation
# trainer.train(general_course_conversation)
trainer.train(courses_conversation)
trainer.train(bachelors_courses_conversation)
trainer.train(master_courses_conversation)
trainer.train(doctoral_courses_conversation)
trainer.train(mphil_courses_conversation)
trainer.train(pgdiploma_courses_conversation)

#training the chatbot with the department_conversation
trainer.train(department_conversation)

#training the chatbot with the examination queries
trainer.train(apply_for_conversations)
trainer.train(convocation_conversations)

#training the chatbot with the admission_notices_converstion
trainer.train(admission_notices_converstion)

#training the chatbot with the eligibility_conversations
trainer.train(eligibility_conversations)

#training the chatbot with the migration_conversations
trainer.train(migration_conversations)

#training the chatbot with the transcripts_conversations
trainer.train(transcripts_conversations)

#training the chatbot with the contact_conversation
trainer.train(contact_conversations)

#training the chatbot with the email_conversation
trainer.train(email_conversations)

#training the chatbot with the hostel_conversation
trainer.train(hostel_conversation)

##Flask app

static_path = 'university/www.unigoa.ac.in'

app = Flask(__name__, template_folder = static_path,static_folder = static_path, static_url_path = '')

@app.route("/")
def index():
    return render_template("index.html") #starting page

@app.route("/get")
def get_bot_response():
    actResponse = ''
    userText = request.args.get("msg") #get data from input
    response = str(bot.get_response(userText))
    # appendfile = os.listdir('saved_conversations')[-1]

    appendfile = open('saved_conversations/'+str(filenumber),"a")
    appendfile.write('user : '+userText+'\n')
    appendfile.write('bot : '+response+'\n')
    appendfile.close()

    return response

if __name__ == "__main__":
    app.run()
