
#############################
#                           #
##          courses        ##
##       conversations     ##
#                           #
#############################

general_course_intents = {
    "intents": [

        {"tag": "program_details",
        "patterns": ["program detail"],
        "responses": ["Choose from below. <br><button onclick='buttonAction(this)'>Bachelors</button><br>\
            <button onclick='buttonAction(this)'>Masters</button><br>\
                <button onclick='buttonAction(this)'>Post Graduate in Diploma</button><br>\
                    <button onclick='buttonAction(this)'>MPhil</button>"]
        },

        {"tag": "bachelor_details",
        "patterns": ["bachelor"],
        "responses": ["The following programs are provided by the University: <br><button onclick='buttonAction(this)'>Bachelor in Commerce (BCOM)</button><br>\
            <button onclick='buttonAction(this)'>Bachelor in Science (BSC)</button><br>\
                <button onclick='buttonAction(this)'>Bachelor in Arts (BA)</button><br>\
                    <button onclick='buttonAction(this)'>Bachelor in Medicine</button><br>\
                        <button onclick='buttonAction(this)'>Bachelor in Engineering (BE)</button><br>\
                            <button onclick='buttonAction(this)'>Bachelor in Law</button><br>\
                                <button onclick='buttonAction(this)'>Bachelor in Computer Applications (BCA)</button>"]
        },


        {"tag": "master_details",
        "patterns": ["master"],
        "responses": ["The following programs are provided by the University: <br><button onclick='buttonAction(this)'>Social Work</button><br>\
            <button onclick='buttonAction(this)'>Library and Information Sciences</button><br>\
                <button onclick='buttonAction(this)'>Computer Applications</button><br>\
                    <button onclick='buttonAction(this)'>Commerce</button><br>\
                        <button onclick='buttonAction(this)'>Business Administration in Financial Servicecs</button><br>\
                            <button onclick='buttonAction(this)'>Sciencesw</button><br>\
                                <button onclick='buttonAction(this)'>Arts</button><br>\
                                    <button onclick='buttonAction(this)'>Medicine</button><br>\
                                        <button onclick='buttonAction(this)'>Management</button><br>\
                                            <button onclick='buttonAction(this)'>Fine Arts</button>"]
        },

    ]

}

courses_intents = {
    "intents": [

        {"tag": "prog_provided",
        "patterns": ["university program provided"],
        "responses": ["The following programs are provided by the University: \
            Bachelors, Masters, Post Graduate in Diploma, MPhil and Doctoral Programmes (Phd). \
                Also there are programs like Study India and Study Japan."]
        },

        {"tag": "study_ind_prgram",
        "patterns": ["india study program"],
        "responses": ["Study India Programme (SIP) started in the year 2003. It consists of basic orientation \
            in English, Indian Culture through Languages and Literature; India\'s History and Philosophy, etc."]
        },
        
        {"tag": "study_ind_prgram_more",
        "patterns": ["study information india programme"],
        "responses": ["Check this link: <a href='academics/a/programmes/study-india-programme.html' \
                    > Study India Programme </a>",
        "Check this link: <a href='/academics/a/programmes/study-india-programme.html'> Study India Programme </a>"]
        },

        {"tag": "study_japan_prgram",
        "patterns": ["study japan tell programme"],
        "responses": ["Study Japan Programme (SJP) is Student Exchange Programme. Under this programme, \
            students study modules on Japanese society, culture, business and communications."]
        },

        {"tag": "study_japan_prgram_more",
        "patterns": ["study japan tell programme"],
        "responses": ["Check this link: <a href='academics/a/programmes/study-japan-programme.html' \
                    > Study Japan Programme </a>",
        "Check this link: <a href='/academics/a/programmes/study-japan-programme.html'> Study Japan Programme </a>"]
        },

    ]
}

bachelors_courses_intents = {
    "intents": [

        {"tag": "bachelor_program",
        "patterns": ["course programme bachelor"],
        "responses": ["Here are some, Bachelor in Commerce (BCOM), Bachelor in Science (BSC), Bachelor in Arts (BA), \
            Bachelor in Medicine, Bachelor in Engineering (BE), Bachelor in Law, \
                Bachelor in Computer Applications (BCA)."]
        },
        
        {"tag": "bachelors_science",
        "patterns": ["bachelor science course available", "provided bachelor science course"],
        "responses": ["Physics, Biotechnology, Zoology, Botany, Chemistry, Matehmatics, Computer Science, Nursing, etc."]
        },

        {"tag": "engineering_option",
        "patterns": ["engineering option"],
        "responses": ["Electronics and Communication, Computer, Mechnical, Civil, Infirmation Technology, etc."]
        },

        {"tag": "bachelors_arts",
        "patterns": ["provided course arts bachelor", "available course arts bachelor"],
        "responses": ["These are the avilable courses in BA: Hindi, Economics, English, History, Konkani, Marathi, etc."]
        },

        {"tag": "bachelors_option",
        "patterns": ["option bachelor"],
        "responses": ["Library and Information Sciences (BLISC), Education, Management, Design, Fine Arts, Vocatioan."]
        },

        {"tag": "bachelors_prog_info",
        "patterns": ["information programme bachelor"],
        "responses": ["Check this link: <a href='academics/programmes/bachelors.html' \
                    > Bachelors Programme </a>"]
        },

        {"tag": "bachelors_bcom_info",
        "patterns": ["bcom commerce bachelor ", "bcom", "commerce bachelor", "information bcom", "information commerce bachelor"],
        "responses": ["Click below buttons to download the syllabus. <br><a href='/uploads/syllabus/87_syllabus_87_revised_1_syllabus_Semester-wise-syllabus...from-1-to-6-Sem..17.5.2013.pdf' download='BCOM Syllabus'><button>Syllabus</button></a><br>\
            <a href='/uploads/syllabus/87_cbcs_syllabus_Syllabus-for-Bachelor-of-Commerce--General--Degree-program-under-CBCS.pdf' download='BCOM CBSC Syllabus'><button>BCOM CBSC Syllabus</button></a><br>\
                <a href='/uploads/syllabus/87_cbcs_2_syllabus_Syllabus-for-Bachelor-of-Commerce--Honours--Degree-program-under-CBCS.pdf' download='BCOM CBSC Syllabus 2'><button>BCOM CBSC Syllabus 2</button></a><br>\
                    Institutions offering this course:<br>\
                        <a href='http://dmscollege.ac.in/' \
                            target='_blank' > Dnyanprassarak Mandal's College of Arts, Sou. Sheela Premanand Vaidya College of Science & V. N. S. Bandekar College of Commerce </a>\
                                <a href='https://www.fragnelcollege.edu.in/' \
                            target='_blank' > Fr. Agnel College of Arts & Commerce</a>\
                                <a href='http://www.khandolacollege.edu.in/' \
                            target='_blank' > Government College of Arts, Science & Commerce, Khandola</a>\
                                <a href='http://www.caculocollege.ac.in/' \
                            target='_blank' > Saraswat Vidyalaya's Sridora Caculo College of Commerce & Management Studies</a>"]
        },
               
        {"tag": "bachelors_science_info",
        "patterns": ["science bsc bachelor", "bsc", "information bsc", "science bachelor", "information science bachelor"],
        "responses": ["The following programs are provided by the University: <br><button onclick='buttonAction(this)'>Bachelor in Commerce (BCOM)</button><br>\
            <button onclick='buttonAction(this)'>B.SC. CHEMISTRY</button><br>\
                <button onclick='buttonAction(this)'>B.SC. BIOTECHNOLOGY</button><br>\
                    <button onclick='buttonAction(this)'>B.SC. BOTANY</button><br>\
                        <button onclick='buttonAction(this)'>B.SC. PHYSICS</button><br>\
                            <button onclick='buttonAction(this)'>B.SC. MATHEMATICS</button><br>\
                                <button onclick='buttonAction(this)'>B.SC. COMPUTER SCIENCE</button>"]
        },

        {"tag": "bsc_chemistry",
        "patterns": ["chemistry bsc", "chemistry science bachelor", "information chemistry bsc", "information chemistry science bachelor"],
        "responses": ["Click below buttons to download the syllabus. <br><a href='/uploads/syllabus/93_syllabus_BSC_Chemistry.zip' download='Bsc Chemistry Syllabus'><button>Syllabus</button></a><br>\
            <a href='/uploads/syllabus/93_cbcs_syllabus_Syllabus-for-B.Sc.-Chemistry--General---Honours--under-CBCS.pdf' download='Bsc Chemistry CBSC Syllabus'><button>BCOM CBSC Syllabus</button></a><br>\
                <a href='/uploads/syllabus/93_cbcs_2_syllabus_Syllabus-of-B.Sc.-Industrial-Chemistry-under-CBCS.pdf' download='Bsc Chemistry CBSC Syllabus 2'><button>BCOM CBSC Syllabus 2</button></a><br>\
                    Institutions offering this course:<br>\
                        <a href='http://dmscollege.ac.in/' \
                            target='_blank' > Dnyanprassarak Mandal's College of Arts, Sou. Sheela Premanand Vaidya College of Science & V. N. S. Bandekar College of Commerce </a>\
                                <a href='https://www.fragnelcollege.edu.in/' \
                            target='_blank' > Fr. Agnel College of Arts & Commerce</a>\
                                <a href='http://www.khandolacollege.edu.in/' \
                            target='_blank' > Government College of Arts, Science & Commerce, Khandola</a>\
                                <a href='http://www.caculocollege.ac.in/' \
                            target='_blank' > Saraswat Vidyalaya's Sridora Caculo College of Commerce & Management Studies</a>"]
        },

        {"tag": "",
        "patterns": ["bsc biotechnology","biotechnology science bachelor", "information bsc biotechnology","information biotechnology science bachelor"],
        "responses": ["Click below buttons to download the syllabus. <br><a href='/uploads/syllabus/bsc-biotechnology_syllabus_10120190520.103232.pdf' download='Bsc Biotechnology Syllabus'><button>Syllabus</button></a><br>\
            <a href='/uploads/syllabus/bsc-biotechnology_revisedsyllabus_10120201026.090652.pdf' download='Bsc Biotechnology Revised Syllabus'><button>Revised Syllabus</button></a><br>\
                <a href='http://dmscollege.ac.in/' \
                    target='_blank' > Dnyanprassarak Mandal's College of Arts, Sou. Sheela Premanand Vaidya College of Science & V. N. S. Bandekar College of Commerce </a>\
                <a href='https://www.fragnelcollege.edu.in/' \
                    target='_blank' > Fr. Agnel College of Arts & Commerce</a>\
                <a href='http://www.khandolacollege.edu.in/' \
                    target='_blank' > Government College of Arts, Science & Commerce, Khandola</a>\
                <a href='http://www.caculocollege.ac.in/' \
                    target='_blank' > Saraswat Vidyalaya's Sridora Caculo College of Commerce & Management Studies</a>"]
        },

    ]
}

master_courses_intents = {
    "intents": [

        {"tag": "masters_program_info",
        "patterns": ["information prgramme masters", "prgramme masters"],
        "responses": ["The following courses are provided in the Master Degree: Social Work, Library and Information Sciences, \
            Computer Applications, Commerce, Business Administration in Financial Servicecs, Sciences, Arts, \
                Medicine, Management and Fine Arts.\
                    Check this link: <a href='academics/programmes/masters.html' \
                        > Master's Programme </a>"]
        },

        {"tag": "masters_science_info",
        "patterns": ["master science", "master option science", "master course science"],
        "responses": ["There are lot of courses provided. Here are some of them, Botany, Zoology, Nursing, \
            Analytical Chemistry, marine Science, Electronics, Mathematics, Physics, etc."]
        },

        {"tag": "master_arts_info",
        "patterns": ["master course arts", "master option arts", "master arts"],
        "responses": ["English, French, History, Konkani, Economics, etc."]
        },

        {"tag": "master_medicine_info",
        "patterns": ["medicine option master", "medicine course master "],
        "responses": ["Ayurvedic Medicine, Pathology, Microbiology, Periodontics, etc."]
        },

    ]
}

# mphil_courses_conversation = {
#     "intents": [

#         {"tag": "",
#         "patterns": [""],
#         "responses": [""]
#         },
#         'Tell about MPhil',
#         'MPhil, Master of Philosophy, is a postgraduate research Masters. Instead of completing taught units \
#             and assessments, an MPhil consists of your own independent project.',

#         {"tag": "",
#         "patterns": [""],
#         "responses": [""]
#         },
#         'Which are the courses provided in the MPhil program?',
#         'Biotechnology, Botany, English, Computer Science, Mathematics, Physics.',

#         {"tag": "",
#         "patterns": [""],
#         "responses": [""]
#         },
#         'Tell more things in MPhil',
#         "Check this link: <a href='academics/programmes/masters-of-philosophy.html' \
#                     > MPhil Programme </a>",
#         "Check this link: <a href='/academics/programmes/masters-of-philosophy.html'> MPhil Programme </a>",
#     ]
# }

# doctoral_courses_conversation = {
#     "intents": [

#         {"tag": "",
#         "patterns": [""],
#         "responses": [""]
#         },
#         'Tell about Doctoral Program',
#         'The following courses are provided in the Doctoral Program: Economics, Botany, English, Law \
#             Chemistry, Commerce, Computer Science, Mathematics, Physics.',

#         {"tag": "",
#         "patterns": [""],
#         "responses": [""]
#         },
#         'Give more information about doctoral programme',
#         "Check this link: <a href='academics/programmes/doctoral-programmes.html' \
#                     > Doctoral Programme </a>",
#         "Check this link: <a href='/academics/programmes/doctoral-programmes.html'> Doctoral Programme </a>",
#     ]
# }

# pgdiploma_courses_conversation = {
#     "intents": [

#         {"tag": "",
#         "patterns": [""],
#         "responses": [""]
#         },
#         'Which courses are provided in PG Diploma',
#         'Medicine, Management Studies and other branches like Agriculture, Computer Applications, etc.',

#         {"tag": "",
#         "patterns": [""],
#         "responses": [""]
#         },
#         'Give more information about PG Diploma',
#         "Check this link: <a href='academics/programmes/pg-diploma.html' \
#                     > PG Diploma Programme </a>",
#         "Check this link: <a href='/academics/programmes/pg-diploma.html'> PG Diploma Programme </a>",
#     ]
# }