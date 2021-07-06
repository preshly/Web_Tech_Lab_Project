contact_intents ={"intents":[
    {
        "tag": "Uni_Contact",
        "patterns": ["university reception number contact","recption contact number","university contact number" ],
        "responses": ["You can contact the University on:<br/> <a href ='tel:+91-8669609048'> +91 8669609048 </a>'"],
    },

    {
        "tag": "VigilanceOfficer_Contact",
        "patterns": ["contact number vigilance officer","vigilance officer"],
        "responses": ["Prof. Usha D. Muraleedharan:<br/> <a href ='tel:+91-8669609240'> +91 8669609240 </a>'"],
    },

    {"tag": "AntiRagging_Contact",
        "patterns": ["antiragging number coordinator contact","contact ragging","report ragging"],
        "responses": ["Prof.K.S.Bhat :<br/> <a href ='tel:+91-8669609103'> +91 8669609103 </a> or <a href ='tel:+91-832-2335208'> +91 832 2335208 </a>'"],
    },
    
    {
        "tag": "Report_SexualHarassment_Contact",
        "patterns": ["harassment sexual report contact number","report sexual harassment","sexual harassment contact"],
        "responses": ["Prof. Savita Kerkar:<br/> <a href ='tel:+91-9326102039'> +91 9326102039 </a>'"],
    },

    {
        "tag": "GUTele_Directory",
        "patterns": ["telephone directory goa university","tele directory"],
        "responses": ["Click Here:<br /> \
        <button type='button' class = 'buttonLink' > \
        <a href ='/uploads/confg_docs/20210416.104425_GU_Phone_email_book_NEW.pdf' style='color:black;' download = 'Gu_Phone_email_book'> Telephone Directory </a> \
        </button>"],
    },


    ]
} 

email_intents = {"intents":[

    {
        "tag": "Uni_email",
        "patterns": ["email address university","university email"],
        "responses": ["You can contact the University via email:<br/> <a href ='mailto:registrar@unigoa.ac.in'> registrar@unigoa.ac.in </a>'"],
    },

    {
        "tag": "vigilanceOfficer_email",
        "patterns": ["email vigilance officer address","email vigilance officer"],
        "responses": ["Prof. Usha D. Muraleedharan:<br/> <a href ='mailto:rusha@unigoa.ac.in'> rusha@unigoa.ac.in </a>"]
    },

    {
        "tag": "Antiragging_email",
        "patterns": ["email coordinator antiragging address","ragging email address","report ragging email"],
        "responses": ["Prof.K.S.Bhat :<br/> <a href ='mailto:sripad@unigoa.ac.in'> sripad@unigoa.ac.in </a>'"]
    },

    {
        "tag": "SexualHarassment_email",
        "patterns": ["email sexual harassment address report","sexual harassment email"],
        "responses": ["Prof. Savita Kerkar:<br/> <a href ='mailto:savita@unigoa.ac.in'> savita@unigoa.ac.in </a>"]
    },


    ]
}

