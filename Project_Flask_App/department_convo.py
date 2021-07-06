
#############################
#                           #
##        department       ##
##      conversations      ##
#                           #
#############################


department_conversation = {"intents": [

    {"tag": "departments",
        "patterns": ["department", "university department", "department detail",
            "university department information", "department information",],
        
        "responses": ["There are 22 departments in the University. Choose from below: \
        <br /> <button type='button' onClick='buttonAction(this) '> Botany Department </button> \
        <br /> <button type='button' onClick='buttonAction(this) '> French Department </button> \
        <br /> <button type='button' onClick='buttonAction(this) '> GBS </button> \
        <br /> <button type='button' onClick='buttonAction(this) '> Hindi Department </button> \
        <br /> <button type='button' onClick='buttonAction(this) '> All Departments and Schools </button>"],
    
    },
   
    # Goa business school
    {"tag": "goa_business_school",
        "patterns": ["GBS", "gbs", "gb", "goa business school", "goa business school information",
            "information about goa business school", "goa business school detail", "gbs detail"],
        
        "responses": ['Goa Business School. <br /> Dean: Professor of Managemnt Studies M.S. Dayanand; <br /> \
        Year of Establishment: 2019; <br /> \
        Office contact: +91-8669609274 (MCom, MBA-FS), +91-8669609280 (MBA, MBA-EXEC), +91-8669609281 (IMBA)\
            +91-8669609138 (Economics), +91-8669609191 (MCA); <br /> \
            Email: msd@unigoa.ac.in; <br /> \
            Programmes: M.Sc Integrated, Integrated MBA(Hospitality, Travel and Tourism), \
                Economics (MA, M.Phil, Ph.D), Commerce (MCom, Ph.D), MCA, MBA, MBA (Executive), MBA FS, \
                Computer Science (M.Phil, Ph.D), Management Studies (M.Phil, Ph.D).' ],
    
    },
       
    # botany
    {"tag": "botany_department",
        "patterns": ["botany department", "information botany department", "botany department information",
            "botany department detail"],
        
        "responses": ['Department of Botany. <br /> HOD: Professor S. Krishnan; <br /> Year of Establishment: 1990; <br /> \
        Office contact: +91-8669609230; <br /> Email: hodbot@unigoa.ac.in; <br /> \
            Programmes: Botany (M.Sc, M.Phil, Ph.D).' ],
    
    },
   
    # Hindi
    {"tag": "hindi_department",
        "patterns": ["hindi department", "information hindi department", "hindi department information", 
            "hindi department detail"],
        
        "responses": ['Department of Hindi. <br /> HOD: Professor Vrushali S. Mandrekar; <br /> \
        Year of Establishment: 1965(CPIR); <br /> \
        Office contact: +91-8669609120; <br /> Email: hodhin@unigoa.ac.in; <br /> \
            Programmes: Hindi (MA, M.Phil, Ph.D).' ],
    
    },
    
    # French
    {"tag": "french_department",
        "patterns": ["french department", "information french department",
            "french department information", "french department detail"],
        
        "responses": ['Department of French and Francophone Studies. <br /> \
        HOD: Associate Professor of Computer Science and Technology Yma F. Pinto; <br /> \
            Year of Establishment: 1965(CPIR); <br /> Office contact: +91-8669609114; <br /> ' ],
    
    },

    {"tag": "french_department_certificate_courses",
        "patterns": ["certificate diploma course offered french department",
            "certificate course offered french department", "french department certificate course",
            "diploma course offered by french department", "french department diploma course"],
        
        "responses": ['Certificate of Proficiency in French-1 (Level A1), <br /> \
        Certificate of Proficiency in French A2 (Level A2), <br /> \
        Diploma of Proficiency in French (Level B1), <br /> Advanced Diploma in French Language (Level B2), \
            <br /> Advanced Diploma in Translation.'],
    
    },
   
    
    {"tag": "all_departments",
        "patterns": ["All Departments and Schools", "department school", ],
        "responses": ["You can check out the information of all the departments from here: \
        <a href='/goa-university-department-listings.html'> Goa University Departments and Schools </a> " ],
    
    },
    
    # chemical sciences
    {"tag": "school_of_chemical_sciences",
        "patterns": ["information school of chemical sciences", "school of chemical sciences", 
            "school chemical sciences", "school chemical science", "school chemical science information", 
            "school chemical science detail"],
        
        "responses": ['School of Chemical Sciences. <br /> Dean: Professor V.S. Nadkarni; <br /> Year of Establishment: 2019; \
        <br /> Office contact: +91-8669609183; <br /> Email: dean.scs@unigoa.ac.in; <br /> \
            Programmes: Chemistry (M.Sc, Ph.D)'],
    
    },
       
    # school of earth, ocean and atmospheric sciences
    {"tag": "school_earth_ocean_atmospheric_sciences",
        "patterns": ["information school of earth, ocean and atmospheric sciences", "school earth ocean atmospheric science", 
            "school of earth, ocean and atmospheric sciences", "school earth ocean atmospheric sciences information",
            "school earth ocean atmospheric sciences detail" ],
        
        "responses": ['School of Earth, Ocean and Atmospheric Sciences. <br /> Dean: Senior Professor of Marine Sciences \
        Harilal B. Menon; <br /> Year of Establishment: 2019; <br /> Office contact: +91-8669609198; <br /> \
            Email: dean.seoas@unigoa.ac.in; <br /> Programmes: Applied Geology (M.Sc), \
                Marine Sciences (M.Sc, M.Phil, Ph.D), Earth Sciences (M.Phil, Ph.D).' ],
    
    },
       
    # biotechnology
    {"tag": "biotechnology department",
        "patterns": ["information biotechnology department", "biotechnology department", "biotechnology department information", 
            "biotechnology department detail"],
        
        "responses": ['Department of Biotechnology. <br /> HOD: Professor Sanjeev C. Ghadi; <br /> Year of Establishment: 2003; \
        <br /> Office contact: +91-8669609246; <br /> Email: hodbiotech@unigoa.ac.in; <br /> \
            Programmes: Biotechnology (M.Sc, M.Phil, Ph.D), Marine Biotechnology (M.Sc).' ],
    
    },   

    # English
    {"tag": "english_department",
        "patterns": ["information english department", "english department", "english department information", 
            "english department detail"],
        
        "responses": ['Department of English. <br /> HOD: Professor K. Sripad Bhat; <br /> Year of Establishment: 1965(CPIR); \
        <br /> Office contact: +91-8669609109; <br /> Email: hodeng@unigoa.ac.in; <br /> \
            Programmes: English (MA, M.Phil, Ph.D).' ],
    
    },
    
    # History
    {"tag": "history_department",
        "patterns": ["information history department", "history department", 
            "history department information", "history department detail"],
        
        "responses": ['Department of History. <br /> HOD: Professor Nagendra Rao; <br /> Year of Establishment: 1965(CPIR); \
        <br /> Office contact: +91-8669609144; <br /> Email: hodhis@unigoa.ac.in; <br /> \
            Programmes: History (MA, M.Phil, Ph.D).'],
    
    },
    
    # school of International Area Studies
    {"tag": "school__international_area_studies",
        "patterns": ["information school International Area Studies", "school international area studies",
            "school of international area studies", 
            "school international area studies information", "school international area studies detail"],
        
        "responses": ['School of International Area Studies. <br /> HOD: Professor Aparajita Gangopadhyay; <br /> \
        Year of Establishment: 2021; <br /> Office contact: +91-8669609160; <br /> \
            Email: hodclas@unigoa.ac.in; <br />\
            Programmes: International Studies (MA, Ph.D), Latin American Studies (M.Phil) \
                and certificate and diploma courses.' ],
    
    },    
    
    {"tag": "school__international_area_studies_certificate_courses",
        "patterns": ["certificate diploma course offered school international area studies",
            "certificate course offered school international area studies", 
            "school of international area studies certificate course",
            "diploma course offered school international area studies", 
            "school international area studies diploma course",],
        
        "responses": ["Certificate of Proficiency in Spanish Language, <br /> Diploma of Proficiency in Spanish Language." ],
    
    },

    # Konkani
    {"tag": "konkani_department",
        "patterns": ["information konkani department", "konkani department", 
            "konkani department information", "konkani department detail"],
        
        "responses": ['Department of Konkani. <br /> HOD: Assocaite Professor Hanumant Chandrakant Chopdekar; <br /> \
        Year of Establishment: 1987; <br /> \
        Office contact: +91-8669609124; Email: hodkon@unigoa.ac.in; <br /> \
            Programmes: Konkani (MA, Ph.D).' ],
    
    },
    
    # Library & Information Science
    {"tag": "library_information_science",
        "patterns": ["information library information science department",
            "library and information science department", "library information science department",
            "library information science department information", 
            "library information science department detail"],
        
        "responses": ['Department of Library & Information Science. <br /> HOD: Professor Ganesha Somayaji; \
        <br /> Year of Establishment: 2013; \
        Office contact: +91-8669609052; <br /> Email: carlos.fernandes@unigoa.ac.in; <br /> \
            Programmes: BLISc, MLISc.' ],
    
    },
      
    # Manohar Parrikar School of Law, Governance & Public Policy
    {"tag": "manohar_parrikar_school_of_law",
        "patterns": ["information manohar parrikar school law governance public policy",
            "Manohar Parrikar School of Law",
            "manohar parrikar school law information", "manohar parrikar school law detail"],
        
        "responses": ['Manohar Parrikar School of Law, Governance & Public Policy. <br /> \
        HOD: Professor of Women\'s Studies Shaila Desouza; <br /> \
        Year of Establishment: 2021; <br /> \
        Office contact: +91-8669609165; <br /> Email: dean.mps@unigoa.ac.in; <br />\
            Programmes: Women\'s Studies (MA, Ph.D).' ],
    
    },
       
    # Marathi
    {"tag": "marathi_department",
        "patterns": ["information marathi department", "marathi department", 
            "marathi department information", "marathi department detail"],
        
        "responses": ['Department of Marathi. <br /> HOD: Associate Professor Sunita S. Umraskar; <br /> \
        Year of Establishment: 1970(CPIR); <br /> \
        Office contact: +91-8669609128; <br /> Email: hodmar@unigoa.ac.in; <br /> \
            Programmes: Marathi (MA, M.Phil, Ph.D).' ],
    
    },
      
    # Microbiology
    {"tag": "microbiology_department",
        "patterns": ["information microbiology department", "microbiology department", 
            "microbiology department information", "microbiology department detail"],
        "responses": ['Department of Microbiology. <br /> HOD: Professor Sandeep Garg; <br /> Year of Establishment: 1974(CPIR);\
        <br /> Office contact: +91-8669609256; <br /> Email: hodmicro@unigoa.ac.in; <br /> \
            Programmes: Microbiology (M.Sc, Ph.D), Biochemistry (M.Sc), Marine Microbiology (M.Sc).' ],
    
    },
    
    
    # Philosophy
    {"tag": "philosophy_department",
        "patterns": ["information philosophy department", "philosophy department", 
            "philosophy department information", "philosophy department detail"],
        "responses": ['Department of Philosophy. <br /> HOD: Professor Koshy Tharakan; <br /> Year of Establishment: 1967(CPIR); \
        <br /> Office contact: +91-8669609148; <br /> Email: hodphl@unigoa.ac.in; <br /> \
            Programmes: Philosophy (MA, M.Phil, Ph.D).' ],
    
    },
     
    # school of physical and applied sciences
    {"tag": "school_physical_applied_sciences",
        "patterns": ["information school physical applied science", 
            "school of physical and applied sciences",
            "school physical applied science information", "school physical applied science detail"],
        
        "responses": ['School of Physical and Applied Sciences. <br /> Dean: Professor of Physics Kaustubh R.S. Priolkar; \
        <br /> Year of Establishment: 2020; <br /> \
            Office contact: +91-8669609214 (Physics), +91-8669609206 (Mathematics), \
                +91-8669609220 (Electronics); <br /> \
            Email: dean.spas@unigoa.ac.in, dean.vice.spas@unigoa.ac.in; <br /> \
                Programmes: Electronics (M.Sc, Ph.D), Mathematics (M.Sc, M.Phil, Ph.D), \
                    Physics (M.Sc, M.Phil, Ph.D) and Vocational Programmes under NSQF.'],
    
    },    
       
    # political science
    {"tag": "political_science_department",
        "patterns": ["information political science department","political science department", 
            "political science department information", "political science department detail"],
        
        "responses": ['Department of Political Science. <br /> HOD: Professor Rahul Tripathi; <br /> \
        Year of Establishment: 1973(CPIR); <br /> \
        Office contact: +91-8669609152; <br /> Email: hodpol@unigoa.ac.in; <br /> \
            Programmes: Political Science (MA, M.Phil, Ph.D).' ],
    
    },
    
    # Portuguese
    {"tag": "portuguese_department",
        "patterns": ["information portuguese department", "portuguese department", 
            "portuguese department information", "portuguese department detail"],
        
        "responses": ['Department of Portuguese & Lusophone Studies. <br /> \
        HOD: Associate Professor of Earth Science Anthony Arthur A. Viegas; <br /> Year of Establishment: 1987;\
        <br /> Office contact: +91-8669609114; <br /> Email: hodpor@unigoa.ac.in; <br /> \
            Programmes: Portuguese (MA, M.Phil, Ph.D) and certificate and diploma courses.'],
    
    },    


    {"tag": "portuguese_department_certificate_courses",
        "patterns": ["certificate diploma course offered portuguese department",
            "certificate course offered portuguese department", 
            "portuguese department certificate course",
            "diploma course offered  portuguese department", 
            "portuguese department diploma course"],
        
        "responses": ['Certificate of Proficiency in Portuguese - I, <br /> Certificate of Proficiency in Portuguese - II, \
        <br /> Diploma of Proficiency in Portuguese, <br /> Advanced Diploma in Portuguese.' ],
    
    },    

    # Sociology
    {"tag": "sociology_department",
        "patterns": ["information sociology department", "sociology department",
            "sociology department information", "sociology department detail"],
        
        "responses": ['Department of Sociology. <br /> HOD: Professor Ganesha Somayaji; <br /> Year of Establishment: 1974(CPIR);\
        <br /> Office contact: +91-8669609156; <br /> Email: hodsoc@unigoa.ac.in; <br />\
            Programmes: Sociology (MA, M.Phil, Ph.D).' ],
    
    },    
    
    #Zoology
    {"tag": "zoology_department",
        "patterns": ["information zoology department", "zoology department", 
            "zoology department information", "zoology department detail"],
        
        "responses": ['Department of Zoology. <br /> HOD: Professor Ramaballav Roy; <br /> Year of Establishment: 1990; \
        <br /> Office contact: +91-8669609263; <br /> Email: hodzoo@unigoa.ac.in; <br />\
            Programmes: Zoology (M.Sc, M.Phil, Ph.D), \
                Post Graduate Diploma in Medical Laboratory Techniques.' ],
    
    },    

    #centre for study of social exclusion
    {"tag": "centre_for_study_of_social_exclusion",
        "patterns": ["information centre study social exclusion inclusive policy",
            "centre for study of social exclusion", "centre for study of social exclusion detail",
            "centre for study of social exclusion information",],
        
        "responses": ['Centre for Study of Social Exclusion & Inclusive Policy. <br /> \
        Co-ordinator: Professor Ganesha Somayaji; <br /> Year of Establishment: 2008; <br />\
        Office contact: +91-8669609094; <br /> Email: csseip@unigoa.ac.in; <br />\
            Faculty: Vijay M. Gawas	Assistant Professor (Tenure).' ],
    
    },    
    
]

}
