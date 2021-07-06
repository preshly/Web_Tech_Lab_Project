general_admin_intents = {"intents": 
    [
        {"tag": "admin_info",
        "patterns": ["information administrative", "info administrative"],
        "responses": ["Choose from below. <button onclick='buttonAction(this)'>Chancellor</button><button onclick='buttonAction(this)'>Vice-Chancellor</button><button onclick='buttonAction(this)'>Finance Officer</button><button onclick='buttonAction(this)'>Registrar</button>"]
        },
        
        {"tag": "chancellor_info",
        "patterns": ["chancellor", "chancellor info", "chancellor information"],
        "responses": ["Bhagat Singh Koshyari<img src='/uploads/leadership/bhagat-singh-koshyari_leadership_2320200907.141316.jpg' alt='Chancellor' /> <br/> <a href='/about-us/leadership/chancellor.html' > Click here </a> for more info"]
        },

        {"tag": "vice-chancellor_info",
        "patterns": ["vice-chancellor", "vice-chancellor information", "vice-chancellor info"],
        "responses": ["Varun Sahni.<img src='/uploads/leadership/varun-sahni_pic_220171225.0717.jpg' alt='Vice-Chancellor'> <br /> <a href='/about-us/leadership/vicechancellor.html' > Click here </a> for more info"]
        },
        
        {"tag": "registrar_info",
        "patterns": ["registrar", "registrar information", "registrar info"],
        "responses": ["Radhika Nayak <img src='/uploads/leadership/radhika-nayak_leadership_2420201214.084052.jpg' alt='Registrar'> <br />  <a href='/about-us/leadership/registrar.html' > Click here </a> for more info"]
        },
        
        {"tag": "finance_officer_info",
        "patterns": ["finance officer", "finance officer information", "finance officer info"],
        "responses": ["Ramesh V. Pai <img src='/uploads/leadership/ramesh-v-pai_leadership_1420190823.145643.jpg' alt='Finance Officer'> <br /> <a href='/about-us/leadership/finance-officer.html' > Click here </a> for more info"]
        },
        
    ]

}
chancellor_intents = {
    "intents": [
        
        {"tag": "chancellor_info",
        "patterns": ["university goa chancellor", "chancellor information","chancellor"],
        "responses": ["The chancellor of Goa University is Bhagat Singh Koshyari.<img src='/uploads/leadership/bhagat-singh-koshyari_leadership_2320200907.141316.jpg' alt='Chancellor'> <br /> <a href='/about-us/leadership/chancellor.html' > \
            Click here </a> for more info"]
        },

        {"tag": "chancellor_email",
        "patterns": ["email chancellor"],
        "responses": ["Chancellors email is governor@rajbhavangoa.org"]
        },

        {"tag": "chancellor_number",
        "patterns": ["number chancellor phone", "contact chancellor phone"],
        "responses": ["Chancellors phone numbers are +91-832-2453506, 2453507, 2453508"]
        },

        {"tag": "chancellor_number",
        "patterns": ["contact number chancellor"],
        "responses": ["Chancellors phone numbers are +91-832-2453506, 2453507, 2453508"]
        },

        {"tag": "chancellor_fax",
        "patterns": ["number fax chancellor"],
        "responses": ["Chancellors fax number is +91-832-2453501"]
        },
 
        {"tag": "who_chancellor",
        "patterns": ["bhagat singh koshiyari"],
        "responses": ["Bhagat Singh Koshiyari is the Chencellor of Goa University"]
        },

    ]
}

vice_chancellor_intents = {
    "intents": [
        
        {"tag": "vc_info",
        "patterns": ["university goa vc", "university goa vicechancellor", "vicechancellor", "vice chancellor"],
        "responses": ["The Vice-Chancellor of Goa University is Varun Sahni.<img src='/uploads/leadership/varun-sahni_pic_220171225.0717.jpg' alt='Vice-Chancellor'> <br /> <a href='/about-us/leadership/vicechancellor.html' > \
            Click here </a> for more info"]
        },

        {"tag": "vc_email",
        "patterns": ["vicechancellor email ", "vc email"],
        "responses": ["Vice-Chancellors email is vc@unigoa.ac.in"]
        },

        {"tag": "vc_contact",
        "patterns": ["number phone vicechancellor", "number phone vc", "number contact vicechancellor", "number contact vc"],
        "responses": ["Vice-Chancellors phone numbers are +91-8669609001"]
        },

        {"tag": "vc_tax",
        "patterns": ["number vicechancellor fax"],
        "responses": ["Vice-Chancellors fax numbers are +91-832-2451184; -2451576; -2453879"]
        },

        {"tag": "who_vc",
        "patterns": ["varun sahni"],
        "responses": ["Hes the Vice-Chencellor of Goa University"]
        },

    ]
}

dean_intents = {
    "intents": [
        
        {"tag": "dean_list",
        "patterns": ["deans list", "deans university"],
        "responses": ["Deans of Goa University are \n 1. Ann Neena George - Education\n 2. V.N. Shet - Engineering \n 3. Nina Calderia - Language and Literature \n 4. Saba Da Silva - Law \n 5. Prabhat Kumar Sharma - Life Science and Environment \n 6. R.G. Wiseman Pinto - Medicine \n 7. Ramarao S. Wagh - Performing, Fine Art and Music \n 8. Gopal Krishna Rao - Pharmacy \n 9. Aniruddha S. Pawar - Planning, Achitecture and Design \n 10. Ganesha Domyaji - Social Science \n 11. M.S. Dayanand - Business School \n 12. Shaila Desouza - Manohar Parrikar School of Law, Governance & Public Policy \n 13. V.S. Nadkarni - Chemical Studies \n 14. Harilal B. Menon - Shool of Earth, Ocean and Atmospheric Science \n 15. Aparajita Gangopadhyay. Visit this link to know more. <a href='/about-us/leadership/deans.html' > click here </a>"]
        },

        {"tag": "dean_education",
        "patterns": ["dean education"],
        "responses": ["Ann Neena George is the dean of Education"]
        },

        {"tag": "dean_engineering",
        "patterns": ["dean engineering"],
        "responses": ["V.N. Shet is the dean of Engineering"]
        },

        {"tag": "dean_lang_literature",
        "patterns": ["language dean literature"],
        "responses": ["Nina Caldeira is the dean of Language and Literature"]
        },

        {"tag": "dean_law",
        "patterns": ["dean law"],
        "responses": ["Saba da Silva is the dean of Law"]
        },
     
        {"tag": "dean_env_sci",
        "patterns": ["dean science evironment"],
        "responses": ["Prabhat Kumar Sharma is the dean of Science and Evironment"]
        },

        {"tag": "dean_medical",
        "patterns": ["medical dean"],
        "responses": ["R.G. Wiseman Pinto is the dean of Medical"]
        },

        {"tag": "dean_fineart",
        "patterns": ["fine art dean performing music"],
        "responses": ["Ramarao Wagh is the dean of Performing, Fine Art and Music"]
        },

        {"tag": "dean_pharmacy",
        "patterns": ["pharmacy dean"],
        "responses": ["Gopal Krishna Rao is the dean of Pharmacy"]
        },

        # {"tag": "",
        # "patterns": [""],
        # "responses": [""]
        # },
        # 'Who is the dean of Planning, Architecture & Design?',
        # 'Aniruddha S. Pawar is the dean of Planning, Architecture & Design',
        
        # {"tag": "",
        # "patterns": [""],
        # "responses": [""]
        # },
        # 'Who is the dean of Social Sciences?',
        # 'Ganesh Somayaji is the dean of Social Sciences',
        
        # {"tag": "",
        # "patterns": [""],
        # "responses": [""]
        # },
        # 'Who is the dean of Goa Business School?',
        # 'M.S. Dayanand is the dean of Goa Business School',
        
        # {"tag": "",
        # "patterns": [""],
        # "responses": [""]
        # },
        # 'Who is the dean of Manohar Parrikar School of Law, Governance & Public Policy?',
        # 'Shaila Desouza is the dean of Manohar Parrikar School of Law, Governance & Public Policy',
        
        # {"tag": "",
        # "patterns": [""],
        # "responses": [""]
        # },
        # 'Who is the dean of School of Chemical Sciences?',
        # 'V.S. Nadkarni is the dean of School of Chemical Sciences',
        
        # {"tag": "",
        # "patterns": [""],
        # "responses": [""]
        # },
        # 'Who is the dean of School of Earth, Ocean & Atmospheric Sciences?',
        # 'Harilal B. Menon is the dean of School of Earth, Ocean & Atmospheric Sciences',
        
        # {"tag": "",
        # "patterns": [""],
        # "responses": [""]
        # },
        # 'Who is the dean of School of International and Area Studies?',
        # 'Aparijita GangopadhyaySchool of Physical and Applied Sciences is the dean of School of International and Area Studies',
        
        # {"tag": "",
        # "patterns": [""],
        # "responses": [""]
        # },
        # 'Who is the dean of School of Physical and Applied Sciences?',
        # 'Kaushtubh R.S. Priolkar is the dean of School of Physical and Applied Sciences',
        
        # {"tag": "",
        # "patterns": [""],
        # "responses": [""]
        # },
        # 'Who is the dean of School of Sanskrit & Indic Knowledge Systems?',
        # 'Vrushali S. Mandrekar is the dean of School of Sanskrit & Indic Knowledge Systems',
        
    ]
}

registrar_intents = {
    "intents": [
        
        {"tag": "registrar_info",
        "patterns": ["goa university registrar", "university registrar"],
        "responses": ["Radhika Nayak is the officiating registrar of Goa University.<img src='/uploads/leadership/radhika-nayak_leadership_2420201214.084052.jpg' alt='Registrar'> <br /> <a href='/about-us/leadership/registrar.html' > \
            Click here </a> for more info"]
        },

        {"tag": "registrar_email",
        "patterns": ["email address registrar"],
        "responses": ["Here is the email registrar@unigoa.ac.in"]
        },

        {"tag": "registrar_phone",
        "patterns": ["phone number registrar", "contact number registrar"],
        "responses": ["Registrars phone number is +91-8669609005 / +91-832-2451097"]
        },

        {"tag": "who_registrar",
        "patterns": ["radhika nayak"],
        "responses": ["Radhika Nayak is the Registrar of Goa University. <a href='/about-us/leadership/registrar.html' > \
            Click here </a> for more info"]
        }

    ]
}

finance_officer_intents = {
    "intents": [
    
        {"tag": "finance_off_info",
        "patterns": ["officer finance university goa", "officer finance"],
        "responses": ["Ramesh V. Pai is the Finance Officer of Goa University.<img src='/uploads/leadership/ramesh-v-pai_leadership_1420190823.145643.jpg' alt='Image of Registrar'> <br /> <a href='about-us/leadership/finance-officer.html' > \
            Click here </a> for more info"]
        },

        {"tag": "finance_off_email",
        "patterns": ["address finance officer email"],
        "responses": ["here is the email fo@unigoa.ac.in"]
        },
    
        {"tag": "finance_off_phone",
        "patterns": ["number phone finance officer", "number contact finance officer", "phone finance officer", "contact finance officer"],
        "responses": ["finance officer phone number is +91-8669609011"]
        },

        {"tag": "who_fin_off",
        "patterns": ["v ramesh pai"],
        "responses": ["Ramesh V. Pai is the Finance Officer of Goa University. <a href='/about-us/leadership/finance-officer.html' > \
            Click here </a> for more info"]
        },

    ]

}