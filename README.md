# Web_Tech_Lab_Project
Project work for the Web Tech Lab for Semester 4, 2021

## Earlier Version
The Goa University Chatbot Using Rasa folder.
<br/>
Building a chatbot for University website using rasa nlp library.
<hr/>

## Current Version
Using the chatterbot library in python.
<br/>
Using flask for backend.
<br/>

Python packages that we used:
<br/>
1)chatterbot
<br/>
2)flask
<br/>
This can be installed using the pip command in terminal, i.e. pip install package_name.
<br/>

The Unigoa cloned website can be found on this link:
<br/>
https://drive.google.com/drive/folders/1ow98IeMDksYGbL_cpeGJnIq1tdb7ZsaU?usp=sharing

<br/>
The same can also be clone using web scraping tools such as Httrack.
<br/>

Place the downloaded folder in the Project_Flask_App folder of this repo.
<br/>

The directory tree should be something like this: <br/>
	
	Web_Tech_Lab_Project\
		
		->Project_Flask_App\
		
			->University_website_folder, this is the folder containing the cloned website\
			->Other files and folders\
		
		->Other files and folders\

<br/>
If this tree is not maintained, then additional configurations need to be done for static file path in flask app, i.e the app.py file.

<br/>
The static_path = 'university/www.unigoa.ac.in' path should be properly configured.
<br/>
Otherwise rendering issues for css, js and other files for the cloned website does not work properly.
<br/>

Place the chatbot_template folder, containing chatbot template and static files, inside the cloned university
website, i.e. inside the university/www.unigoa.ac.in/ folder and make necessary changes so that the chatbot 
template is displayed on all the university web pages.
<br/>

To run the flask app, type the command in the terminal:
	- python chatbot.py
This will train the chatterbot and store the conversations in db, file based, and also run the flask server.
<br/>

Thanks!

