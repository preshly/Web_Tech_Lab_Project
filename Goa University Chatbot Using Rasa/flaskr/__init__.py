import os

from flask import Flask, render_template, request, jsonify, Response
import requests


def create_app(test_config=None):
    output=[]#("message university","hi")]
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/chatbot')
    def createChatBox():
        return render_template('chatbot.html')


    @app.route('/result',methods=["POST","GET"])
    def Result():
        if request.method=="POST":
            print(list(request.form.values()))
            result=list(request.form.values())[0]
            if result.lower()=="restart":
                output.clear()
            else:
                try:
                    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": result})
                    print("Bot says, ")
                    for i in r.json():
                        bot_message = i['text']
                        print(f"{i['text']}")
                    output.extend([("message university",result),("message stark",bot_message)])
                except:
                    output.extend([("message university", result), ("message stark", "We are unable to process your request at the moment. Please try again...")])

            print(output)
            return render_template("chatbot.html",result=output)


    return app