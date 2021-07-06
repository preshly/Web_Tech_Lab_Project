
#################################
#                               #
##       nltk convo class;     ##
##  get base form of message;  ##
##        then matching.       ##
#                               #
#################################

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


class Nltk_Convo:

    def __init__(self) -> None:
        self.all_data = [hostel_intents, greetings_intents, academic_intents, migration_intents, transcripts_intents, 
            contact_intents,email_intents, general_college_intents, general_edu_institution_intents,
            professional_edu_institution_intents,recognised_edu_institution_intents, general_admin_intents, chancellor_intents, 
            vice_chancellor_intents, dean_intents, registrar_intents, finance_officer_intents,
            admission_notices_converstion, department_conversation, apply_for_conversations, convocation_conversations]
        

        self.labels = []
        self.labels_keywords = []
        self.label_responses = dict()

        self.patterns = []
        self.pattern_intent = []

        self.english_stopwords = stopwords.words('english')
        self.english_stopwords.extend(['provide', 'give', ])

        self.punctuations = re.compile(r"[-_?!:;,.|@#$%^&*<>\\/()'0-9]")

        self.word_lematizer = WordNetLemmatizer()

        self.build_db()

    def filter_tokens(self, words_tokens):
        '''
            function to remove the punctuations and english stopwords from the tokenized words.
            
        '''

        post_punctuation = []
        post = []
        for words in words_tokens:
            word = self.punctuations.sub('', words)
            word = self.word_lematizer.lemmatize(word)

            # print(word)
            if len(word) > 0:
                post.append(word.casefold())
                if word.casefold() not in self.english_stopwords:
                    post_punctuation.append(word.casefold())
        
        # print('post_punctuation: ', end='')
        # print(post_punctuation, end='\n\n')
        if len(post_punctuation) == 0:
            post_punctuation = post
        
        return post_punctuation

    def build_db(self):
        """
            function to build the db.
            import the conversations sets from the files and apply nltk methods on them
        """
    
        print('building db -------------------------')

        for data in self.all_data:
            for intent in data["intents"]:
                if intent["tag"] not in self.labels:
                    self.labels.append(intent["tag"])
                    self.label_responses[intent['tag']] = intent['responses']
                
                intent_keywords = []
                for pattern in intent["patterns"]:
                    pattern_tokens = word_tokenize(pattern) #tokenize
                    pattern_tokens = set(pattern_tokens)

                    if pattern_tokens not in intent_keywords:
                        intent_keywords.append(pattern_tokens)                   
                    

                    self.patterns.append(pattern_tokens)
                    self.pattern_intent.append(intent["tag"])
                
                self.labels_keywords.append(intent_keywords)
        

        print('------------------------')
        for i in range(len(self.labels)):
            print(str(self.labels[i]) + ' \t ' + str(self.labels_keywords[i]), end='\n\n')
        
        print('------------------------')
        

        print('patterns \n' + str(self.patterns), end='\n\n')
        print(len(self.patterns))


        with open("data.pickle", "wb") as f:
            pickle.dump((self.labels, self.labels_keywords, self.label_responses, self.patterns, self.pattern_intent), f)
        print('-----------------------')

    #chat response to send to flask app
    def chat_response(self, given_input):
        '''
            function to process the user input to the chatbot.
            return the chatbot response.
        '''
        
        input_tokens = word_tokenize(given_input)
        input_tokens_filtered = self.filter_tokens(input_tokens)
        input_tokens_filtered = set(input_tokens_filtered)

        print(input_tokens_filtered)
        
        perc_words = [0 for _ in range(len(self.patterns)) ]
        for i in range(len(self.patterns) ):
            perc_words[i] = round( len(input_tokens_filtered.intersection(self.patterns[i] ) )  / len(self.patterns[i] ), 2)

            # perc_words[i] = round( len(input_tokens_filtered.intersection(self.patterns[i] ) )  / len(input_tokens_filtered ), 2)
        
        print(perc_words)
        # results_index = numpy.argmax(perc_words)
        
        results_index = self.find_max_matching_index(perc_words)

        print('index: ' + str(results_index) + '\tvalue: ' +str(perc_words[results_index]))


        tag = self.pattern_intent[results_index]

        responses = self.label_responses[tag]

        response = "I am sorry, but I do not understand."
        
        if perc_words[results_index] > 0.80:
            print('tag: ' + str(tag))
            print(self.patterns[results_index])                    
            
            response = random.choice(responses)
        
        elif perc_words[results_index] >= 0.50:
            print('tag: ' + str(tag))
            print(self.patterns[results_index])

            user_patterns = []
            for i in range(len(self.pattern_intent)):
                if self.pattern_intent[i] == tag:
                    user_patterns.append(self.patterns[i])
            
            perc_words = [0 for _ in range(len(user_patterns)) ]
            for i in range(len(user_patterns) ):

                perc_words[i] = round( len(input_tokens_filtered.intersection(user_patterns[i] ) )  / len(input_tokens_filtered ), 2)
            
            print(perc_words)
            # results_index = numpy.argmax(perc_words)
            
            results_index = self.find_max_matching_index(perc_words)

            print('index: ' + str(results_index) + '\tvalue: ' +str(perc_words[results_index]))       

            if perc_words[results_index] > 0.5:
                response = random.choice(self.label_responses[tag])            
            
        
        return response

    def find_max_matching_index(self, perc_words):
        '''
            method to find the max index matching. Find the max at the end of the list.
        '''
        len_perc_words = len(perc_words)
        max_perc_words = max(perc_words)
        for i in range(len_perc_words):
            if perc_words[i] >= max_perc_words:
                results_index = i

        return results_index



#try in terminal
if __name__ == '__main__':
    cl = Nltk_Convo()    

    while True:
        print('========================')
        inp = input('You: ')
        if inp == 'q':
            break

        
        print('Bot: ' + str(cl.chat_response(inp)) )
        print('------------------------\n')
