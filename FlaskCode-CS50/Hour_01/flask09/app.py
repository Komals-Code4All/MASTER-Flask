
from flask import Flask, render_template, request

''' render_templates automatically looks for html files in the templates file'''
''' request.args reads the arguements passed into the URL '''

''' 
This version uses html form to pass query data to the web page
'''


app = Flask(__name__)   # tell Flask to make this code a web application

# decorators - wrap a function inside another function
@app.route("/")
def index():

    htmlPage = render_template("index.html")
    return htmlPage

@app.route("/greet", methods=[ "POST"]) # allow POST method
def greet():

#    name=request.args.get("name", "World")
    name=request.form.get("name", "World")      # use the FORMs args
    htmlPage = render_template("greet.html", name=name)
    return htmlPage

