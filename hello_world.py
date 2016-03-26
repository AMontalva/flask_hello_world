from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hi_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placehold.it/350x150">
    """
    return html.format(name.title())

@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    jedi_name = last[0:3] + first[0:2]
    html = """
        <h1>
            Hello {}!
        </h1>
    """
    return html.format(jedi_name.title())

app.run(host=environ['IP'],
        port=int(environ['PORT']))