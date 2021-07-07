
import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk import word_tokenize
from nltk import pos_tag, ne_chunk
from nltk.corpus import stopwords
from nltk.stem import wordnet, WordNetLemmatizer

import numpy
import random
import json
import pickle
import re
from datetime import datetime

from hostel_convo import hostel_intents
from greetings_convo import greetings_intents
from contact_conv import contact_intents,email_intents
from college_convo import general_college_intents,professional_edu_institution_intents,general_edu_institution_intents, \
    recognised_edu_institution_intents
from academic_matter_conv import academic_intents, migration_intents, transcripts_intents
from admin_conversation import general_admin_intents, chancellor_intents, vice_chancellor_intents, \
    dean_intents, registrar_intents, finance_officer_intents
from admission_convo import admission_notices_converstion
from department_convo import department_conversation
from examination_conv import apply_for_conversations, convocation_conversations
from courses_convers import general_course_intents, courses_intents, bachelors_courses_intents, master_courses_intents


class Nltk_Convo:

    def __init__(self) -> None:
        self.all_data = [hostel_intents, greetings_intents, academic_intents, migration_intents, transcripts_intents, 
            contact_intents,email_intents, general_college_intents, general_edu_institution_intents,
            professional_edu_institution_intents,recognised_edu_institution_intents, general_admin_intents, chancellor_intents, 
            vice_chancellor_intents, dean_intents, registrar_intents, finance_officer_intents,
            admission_notices_converstion, department_conversation, apply_for_conversations, convocation_conversations,
            general_course_intents, courses_intents, bachelors_courses_intents, master_courses_intents
]
        
        self.words = []
        self.labels = []
        self.docs_x = []
        self.docs_y = []

        self.english_stopwords = stopwords.words('english')
        self.english_stopwords.extend(['provide', 'give', ])

        self.punctuations = re.compile(r"[-_?!:;,.|@#$%^&*<>\\/()'0-9]")

        self.word_lematizer = WordNetLemmatizer()

        self.build_db()

    def remove_punctuations(self, words_tokens):
        '''
            function to remove the puncations from the tokenixed words.
            
        '''

        post_punctuation = []
        for words in words_tokens:
            word = self.punctuations.sub('', words)

            if len(word) > 0:
                post_punctuation.append(word.casefold())
        
        return post_punctuation


    def build_db(self):
        '''
            function to build the db.
            import the conversations sets from the files and apply nltk methods on them
        '''
    
        print('building db -------------------------')

        for data in self.all_data:
            for intent in data["intents"]:
                for pattern in intent["patterns"]:
                    words_tokens = word_tokenize(pattern) #tokenize

                    words_tokens_puncs = self.remove_punctuations(words_tokens) #remove punctuations from words
                    
                    words_tokens_tags_ner = ne_chunk( pos_tag(words_tokens_puncs) ) #pos; ner => named entity
                    words_tokens_tags_ner = set([str(ner) for ner in words_tokens_tags_ner]) #convert to set

                    self.words.extend(words_tokens)
                    self.docs_x.append(words_tokens_tags_ner)
                    self.docs_y.append(intent["tag"])

                    if intent["tag"] not in self.labels:
                        self.labels.append(intent["tag"])
        
        print('words \n' + str(self.words), end='\n\n')
        print('labels \n' + str(self.labels), end='\n\n')
        print('docs_x \n' + str(self.docs_x), end='\n\n')
        print(len(self.docs_x))
        print('docs_y \n' + str(self.docs_y), end='\n\n')

        # try:
        #     # goToExcept if no database, i.e. data.pickle file
        #     with open("data.pickle", "rb") as f:
        #         self.words, self.labels, self.docs_x, self.docs_y = pickle.load(f)
        # except Exception as e:
        #     with open("data.pickle", "wb") as f:
        #         pickle.dump((self.words, self.labels, self.docs_x, self.docs_y), f)
        
        with open("data.pickle", "wb") as f:
            pickle.dump((self.words, self.labels, self.docs_x, self.docs_y), f)


    #chat response to send to flask app
    def chat_response(self, given_input):
        '''
            function to process the user input to the chatbot.
            return the chatbot response.
        '''

        # try:
        #     # goToExcept if no database, i.e. data.pickle file
        #     with open("data.pickle", "rb") as f:
        #         self.words, self.labels, self.docs_x, self.docs_y = pickle.load(f)
        # except Exception as e:
        #     self.build_db()

        input_tokens = word_tokenize(given_input)
        input_tokens_puncs = self.remove_punctuations(input_tokens)

        post_punctuation = []
        post = []
        for words in input_tokens_puncs:
            word = self.punctuations.sub('', words)
            word = self.word_lematizer.lemmatize(word)

            # print(word)
            if len(word) > 0:
                post.append(word.casefold())
                if word.casefold() not in self.english_stopwords:
                    post_punctuation.append(word.casefold())
        
        print('post_punctuation: ', end='')
        print(post_punctuation, end='\n\n')
        if len(post_punctuation) == 0:
            post_punctuation = post
        

        input_tokens_tags_ner = ne_chunk( pos_tag(post_punctuation) )
        input_tokens_tags_ner = set([str(ner) for ner in input_tokens_tags_ner])

        print('\n input tokens; pos; ner: ' + str(input_tokens_tags_ner), end='\n')

        perc_words = [0 for _ in range(len(self.docs_x)) ]
        for i in range(len(self.docs_x) ):
            perc_words[i] = round( len(input_tokens_tags_ner.intersection(self.docs_x[i] ) )  / len(self.docs_x[i] ), 2)
        
        print(perc_words)
        # results_index = numpy.argmax(perc_words)
        
        results_index = self.find_max_matching_index(perc_words)

        print('index: ' + str(results_index) + '\tvalue: ' +str(perc_words[results_index]))


        tag = self.docs_y[results_index]

        for data in self.all_data:
            for tg in data["intents"]:
                if tg["tag"] == tag:
                    user_patterns = tg['patterns']
                    responses = tg['responses']

        response = "I am sorry, but I do not understand."
        
        if perc_words[results_index] > 0.80:
            print('tag: ' + str(tag))
            print(self.docs_x[results_index])                    
            
            response = random.choice(responses)
        
        elif perc_words[results_index] >= 0.50:
            print('tag: ' + str(tag))
            print(self.docs_x[results_index])
            
            if user_patterns:
                input_set = set(given_input.split(' '))

                print(input_set)

                for pattern in user_patterns:
                    print(input_set.intersection(set(pattern.split(' '))) )        

                perc_user_input = [round( len(input_set.intersection(set(pattern.split(' ')) ) ) / len(set(pattern.split(' ')) ), 2) \
                    for pattern in user_patterns] 

                print(perc_user_input)
                # perc_user_input_index = numpy.argmax(perc_user_input)

                perc_user_input_index = self.find_max_matching_index(perc_user_input)               
                
                if perc_user_input[perc_user_input_index] > 0.5:
                    print(perc_user_input_index)
                    response = random.choice(responses)
        
        return response

    def find_max_matching_index(self, perc_words):
        '''
            method to find the max index matching. Find the max at the end of the list.
        '''
        len_perc_words = len(perc_words)
        max_perc_words = max(perc_words)
        results_index = [i for i in range(len_perc_words) if perc_words[i] >= max_perc_words]
        results_index = max(results_index)

        return results_index

#try in terminal
if __name__ == '__main__':
    cl = Nltk_Convo()
    
    while True:
        inp = input('You: ')
        if inp == 'bye':
            break
        print(cl.chat_response(inp))

