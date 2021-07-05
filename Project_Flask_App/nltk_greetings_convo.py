
"""
    {"tag": "",
        "patterns": ["",],
        "responses": ["", ],
    
    },
"""


greetings_intents = {"intents": [
    {"tag": "greet",
        "patterns": ["Hello", "Hi", "Hi there", "hi there","Anyone there", "anyone home", "whats up"],
        "responses": ["Hi there! What can I do for you?", "Hi! How can I help you?", ]
    
    },

    {"tag": "about_well_being",
        "patterns": ["How are you doing?", "How are you", "Are you ok", "Are you fine"],
        "responses": ["I'm doing great.", "I'm fine", "Appreciate you asked. I'm fine", "I'm good", ],
    
    },

    {"tag": "appreciate",
        "patterns": ["That is good to hear", "cool", "awesome", "nice"],
        "responses": ["Thank you", "Thanks"],
    
    },

    {"tag": "goodbye",
        "patterns": ["Good Bye", "good bye", "bye", "I have to go", "I'm leaving", "I have to leave"],
        "responses": ["Good Bye", "Bye", "See you soon", ],
    
    },

    {"tag": "what_can_you_do",
        "patterns": ["what can you do", "what else can you do" ,"How can you help me" ],
        "responses": ["What would you like to know? <br> \
            <button onclick='buttonAction(this)'>Administrative information</button>\
            <br><button onclick='buttonAction(this)'>Program details</button>\
            <br><button onclick='buttonAction(this)'>Department details</button>\
            <br><button onclick='buttonAction(this)'>College Details</button> " ],
    
    },
]
}