
#############################
#                           #
##        greetings        ##
##      conversations      ##
#                           #
#############################

from datetime import datetime

greetings_intents = {"intents": [
    {"tag": "greet",
        "patterns": ["hello", "hi", "anyone home"],
        "responses": ["Hi there! What can I do for you?", "Hi! How can I help you?", ]
    
    },

    {"tag": "about_well_being",
        "patterns": ["how are you doing", "how are you"],
        "responses": ["I'm doing great.", "I'm fine", "Appreciate you asked. I'm fine", "I'm good", ],
    
    },

    {"tag": "appreciate",
        "patterns": ["good", "thanks", "thank", "cool", "awesome", "nice"],
        "responses": ["Thank you", "Thanks"],
    
    },

    {"tag": "goodbye",
        "patterns": ["good bye", "bye", "leaving"],
        "responses": ["Good Bye", "Bye", "See you soon", ],
    
    },

    {"tag": "what_can_you_do",
        "patterns": ["what can you do", "help" ],
        "responses": ["What would you like to know? <br> \
            <button onclick='buttonAction(this)'>Administrative information</button>\
            <br><button onclick='buttonAction(this)'>Program details</button>\
            <br><button onclick='buttonAction(this)'>Department details</button>\
            <br><button onclick='buttonAction(this)'>College Details</button> " ],
    
    },

    {"tag": "today_date",
        "patterns": ["today date", "date today", "date"],
        "responses": [ str( datetime.now().date() ) ],
    
    },
    {"tag": "time_now",
        "patterns": ["time", "current time"],
        "responses": [ str( datetime.now().time().strftime('%H:%M:%S') ) ],
    
    },

]
}