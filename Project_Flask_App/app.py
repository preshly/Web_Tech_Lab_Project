
import os
from flask import Flask, render_template, request, jsonify, Response


static_path = '../Website/Unigoa_website_clone/www.unigoa.ac.in/'
app = Flask(__name__,template_folder=static_path,
            static_folder=static_path,
            static_url_path='' )           


@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)