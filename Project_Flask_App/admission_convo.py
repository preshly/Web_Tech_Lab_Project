
#################################
#                               #
##      admission noticies     ##
##        conversations        ##
#                               #
#################################


admission_notices_converstion = {"intents": [
    {"tag": "university_admission",
    "patterns": ["information admission process university", "university admission detail", 
        "procedure apply university",  "admission process university", "information admission university",
        "university admission info", "admission information", "admission detail", "admission info"],
    
    "responses": ["For general instructions about admission, check here: \
    <a href='/systems/c/admissions/general-instructions.html'> Admission Instructions </a> \
    <br /> \
    For latest announcements about admission, check here: \
        <a href='/systems/c/admissions/announcementsnotices.html'> Admission Announcements </a> \
        <br /> \
    For admission of international students, check here: \
        <a href='/systems/c/admissions/international-students.html'> \
            Admission for International Students </a> \
        <br /> "],
    
    },  

    {"tag": "more_admission_notices",
        "patterns": ["admission notice", "admission notices", "more admission notice",
            "other admission notice" ],

        "responses": ["Click here: <a href='/systems/c/admissions/announcementsnotices.html'> \
        Admission Notices </a>" ],
    
    },
    
    
    {"tag": "admission_notice",
        "patterns": ["university admission notice", "university admission notices" ],
        
        "responses": ["Choose from below: \
        <br /> <button type='button' onClick='buttonAction(this)'> Instructions to selected candidates</button> \
        <br /> <button type='button' onClick='buttonAction(this)'> MCA Admissions April 2021</button> \
        <br /> <button type='button' onClick='buttonAction(this)'> Ph.D. Admissions April 2021 </button> \
        <br /> <button type='button' onClick='buttonAction(this)'> MBA programme 2021-2023 </button> \
        <br /> <button type='button' onClick='buttonAction(this)'> More Admission Notices</button> \
        " ],
    
    },
  
    {"tag": "selected_candidate_instructions",
        "patterns": ["instruction selected candidate", "instructions selected candidate",
            "instruction selected candidate gu art exam",
            "instruction selected candidate university entrance exam", ],
        
        "responses": ["Click here: <br /> \
        <button type='button' class='buttonLink'> \
            <a href='/uploads/confg_docs/20210416.121123_Instructions_Round-I_GU-ART.pdf' download='Instructions_Round-I_GU-ART'> \
            Instructions to selected candidates </a> \
            </button> " ],
    
    },
    
    
    {"tag": "mca_admissions_2021",
        "patterns": ["mca admissions april 2021", "mca admission april", "mca admission", "apply mca",
            "mca admission notice", "mca application", "mca admission info", "mca admission information",
            "mca detail", "MCA Admissions April 2021"],
        
        "responses": ["Click here: <br /> \
        <button type='button' class='buttonLink'> \
            <a href='/uploads/confg_docs/20210415.042437_Notification_MCA_Admission_21-22.pdf' download='MCA_Admission_21-22' > \
            MCA Admissions April 2021 </a> \
            </button>" ],
    
    },
   
    
    {"tag": "phd_admission_2021",
        "patterns": ["Ph.D. Admissions April 2021 ", "Ph.D. admissions april", "phd admission april", 
            "apply phd programme university", "apply phd courses", "Ph.D. admission", "phd admissions", 
            "apply phd", "apply phd university", "phd detail"],
        
        "responses": ["Click here: <br /> \
        <button type='button' class='buttonLink'> \
            <a href='/uploads/confg_docs/20210407.054805_Notification_PhD_Admission_Apr_2021.pdf' download='PhD_Admission_Apr_2021'> \
            Ph.D. Admissions April 2021 </a> \
            </button>" ],
    
    },
   
    
    {"tag": "mba_2021_2023",
        "patterns": ["mba programme 2021-2023", "mba programme", "apply mba programme", "apply mba",
            "university mba programme", "mba programme detail", "mba detail"],
        
        "responses": ["Click here: <br /> \
        <button type='button' class='buttonLink'> \
            <a href='/uploads/confg_docs/20210212.071244_Notification_MBA-prog_2021_final_v_1-2.pdf' download='MBA-prog_2021_final_v_1-2'> \
            MBA programme 2021-2023 </a> \
            </button> "],
    
    },

    
]

}
