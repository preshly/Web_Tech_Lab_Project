
#################################
#                               #
##    apply for certificates   ##
##        conversations        ##
#                               #
#################################

apply_for_conversations = {"intents": [

    {"tag": "examination_query",
        "patterns": ["examination query", "exmaination related query", "exam query",
            "certificate marksheet"],
        
        "responses": ["Choose from the following. Apply for: \
        <br /> <button type='button' onClick='buttonAction(this)'> Answer Book Photocopy </button> \
        <br /> <button type='button' onClick='buttonAction(this)'> Degree Certificate </button> \
        <br /> <button type='button' onClick='buttonAction(this)'> Documents Authentication </button> \
        <br /> <button type='button' onClick='buttonAction(this)'> Duplicate Marksheets & Certificates </button> \
        <br /> <button type='button' onClick='buttonAction(this)'> Verification of Answer Book </button> ", ],
    
    },
        
    
    # add id #afab to the systems/a/examinations/apply-for/answer-book-photocopies.html page
    {"tag": "answer_book_photocopy",
        "patterns": ["answer book photocopy", " apply answer book photocopy",
            "procedure apply answer book photocopy"],
        
        "responses": ["Check this link: <a href='/systems/a/examinations/apply-for/answer-book-photocopies.html#afab'> \
        Apply for Answer Book Photocopies </a>",],
    
    },
    
    
    {"tag": "degree_certificate",
        "patterns": ["degree certificate", "apply degree certificate", "procedure apply degree certificate"],
        
        "responses": ["Check this link: <a href='/systems/a/examinations/apply-for/degree-certificate.html#1'> \
            Apply for Degree Certificate </a>", ],
    
    },
    
    
    {"tag": "documents_authentication",
        "patterns": ["document authentication", "procedure document authentication",
            "document authentication details",],
        
        "responses": ["There are two ways, Online and Manual. Check this link: \
            <a href='/systems/a/examinations/apply-for/documents-authentication.html'> \
                Documents Authentication </a>", ],
    
    },
    
    
    
    # add id #dupct to the systems/a/examinations/apply-for/duplicate-marksheets-certificates.html page
    {"tag": "duplicate_marksheets",
        "patterns": ["Duplicate Marksheets & Certificates", "duplicate marksheet certificate", 
            "apply duplicate marksheet", "detail get duplicate marksheet" ],
        
        "responses": ["Check this link: <a href='/systems/a/examinations/apply-for/duplicate-marksheets-certificates.html#dupct'> \
            Apply for Duplicate Marksheets & Certificates </a>", ],
    
    },
    
    
    
    {"tag": "verification_answer_book",
        "patterns": ["verification answer book", "answer book verification information"],
        
        "responses": ["Check this link: \
            <a href='/systems/a/examinations/apply-for/reevaluationverification-of-answer-books.html#1'> \
            Re-evaluation & Verification of Answer Books </a>", ],
    
    },    
        
]

}

convocation_conversations = {"intents": [
    {"tag": "university_convocation",
        "patterns": ["information university convocation", "information convocation", 
            "university convocation", "convocation detail"],
        
        "responses": ["Check this link: <a href='/systems/c/examinations/convocation.html'> Convocation </a>"],
    
    },
    
]

}