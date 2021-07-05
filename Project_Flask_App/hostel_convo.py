
#############################
#                           #
##          hostel         ##
##      conversations      ##
#                           #
#############################

hostel_intents = {"intents": [
        {"tag": "hostel_details",
        "patterns": ["hostel detail", "hostel info", "hostel information", "hostel"],
        
        "responses": ["Choose from the following options of hostel: \
            <br /> <button type='button' onClick='buttonAction(this)'> Chief Warden's</button> \
            <br /> <button type='button' onClick='buttonAction(this)'> Hostel Warden's</button> \
            <br /> <button type='button' onClick='buttonAction(this)'> Hostel Facilities </button> \
            <br /> <button type='button' onClick='buttonAction(this)'> Hostel Admission </button> \
            <br /> <button type='button' onClick='buttonAction(this)'> Hostel Fee </button> \
            <br /> <button type='button' onClick='buttonAction(this)'> Hostel Rules </button> \
            <br /> <button type='button' onClick='buttonAction(this)'> Mess Charges </button> \
        <br /> <button type='button' onClick='buttonAction(this)'> Hostel Application Form </button> "],
        },

        {"tag": "chief_wardens",
        "patterns": ["chief warden", "hostel chief warden", "chief warden detail", 
            "chief warden info", "chief warden information"],
        
        "responses": ["Professor Nilesh A. Borde, Chief Warden Men's Hostels \
            <br /> <img src= '/uploads/deps_academic/nilesh-a_pic_15920171120.1009.jpg' alt='chief_warden' />\
            <br /> Professor Savita S. Kerkar, Chief Warden Women's Hostels \
            <br /> <img src= '/uploads/deps_academic/savita-s-kerkar_staff_acadpic_7620180122.1048.jpg' alt='chief_warden'/>\
            "]
        },

        {"tag": "wardens",
        "patterns": ["wardens", "warden detail", "hostel warden detail", "hostel warden", "university hostel warden"
            "warden info", "warden information"],
        
        "responses": ["Dr. Narayan T. Vetrekar, Warden Men's Hostels \
            <br /> <img src= '/uploads/deps_academic/narayan-t-vetrekar_staff_acadpic_14820190912.145959.jpg' alt='warden' />\
            <br /> Ms. Pallavi P. Gaude, Warden Women's Hostel \
            <br /> <img src= '/uploads/deps_academic/pallavi-pandhari-gaude_staff_acadpic_22020180911.144526.jpg' alt='warden'/>\
            <br /> Ms. Sulochana S. Pednekar, Warden Research Scholars Hostels \
            <br /> <img src= '/uploads/deps_academic/sulochana-suresh-pednekar_staff_acadpic_18520180629.162809.jpg' alt='warden'/>\
            "]
        },

        {"tag": "hostel_facility",
        "patterns": ["hostel facilities", "university hostel facility", "hostel facility", "facilities hostel provides"],
        "responses": ["Check here: <a href='/facilities/hostelsmess.html#faci' > Hostel Facilities </a>"]
        },

        {"tag": "hostel_admission",
        "patterns": ["hostel admission", "hostel admission detail", "apply hostel", "hostel admission detail",
            "hostel admission information", "hostel admission info" ],
        
        "responses": ["Check here: <a href='/facilities/hostelsmess.html#admission' > Hostel Admission </a>"]
        },

        {"tag": "hostel_fee",
        "patterns": ["hostel fee", "hostel fee detail", "hostel fee info", "hostel fee information", "mess charge"],
        "responses": ["Check here: <a href='/facilities/hostelsmess.html#Fee' > Hostel Fee </a>"]
        },

        {"tag": "hostel_rules",
        "patterns": ["hostel rule", "university hostel rule"],
        "responses": ["Check here: <a href='/facilities/hostelsmess.html#rules' > Hostel Rules </a>"]
        },

        {"tag": "hostel_application_form",
        "patterns": ["hostel application form", "university hostel application form"],
        "responses": ["Check here: <br /> \
            <button type='button' class='buttonLink'> \
                <a href='/uploads/confg_images/20171215.1242_Hostel_Application_Form.pdf' download='Hostel_Application_Form'> Hostel Application Form </a> \
                </button>"]
        }
        
    ]
}