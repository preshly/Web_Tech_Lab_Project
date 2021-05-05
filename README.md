# Web_Tech_Lab_Project
This is a project work for the Web Tech Lab for Semester 4, 2021

## Earlier Version
The Goa University Chatbot Using Rasa folder\
Building a chatbot for University website using rasa nlp library.\

## Current Version
Using the chatterbot library in python.\
Using flask for backend.\

Python packages that we used:\
1)Chatterbot\
2)flask\
This can be installed using the pip command in terminal, i.e. pip install package_name.\

The Unigoa cloned website can be found on this link:\
https://drive.google.com/drive/folders/1ow98IeMDksYGbL_cpeGJnIq1tdb7ZsaU?usp=sharing

<br/>
The same can also be clone using web scraping tools such as Httrack.\

Place the downloaded folder in the parent folder outside the Project_Flask_App folder.\

The directory tree should be something like this:\
	
	Web_Tech_Lab_Project\
		
		->Project_Flask_App\
		
		->Chatbot, this is the folder containing the cloned website\
		
		->Other files and folders\

<br/>
If this tree is not maintained, then additional configurations need to be done for static file path in flask app, i.e the app.py file.\

<br/>
The static_path = '../Website/Unigoa_website_clone/www.unigoa.ac.in/' path should be properly configured.\

Otherwise rendering issues for css, js and other files for the cloned website does not work properly.

