
from flask import Flask, render_template, request

''' render_templates automatically looks for html files in the templates file'''
''' request.args reads the arguements passed into the URL '''

''' 
Passing a query to the server URL   
    http://127.0.0.1:5000/?name=%22komal%22 

    
    without ?name=""   works now
'''


app = Flask(__name__)   # tell Flask to make this code a web application

# decorators - wrap a function inside another function
@app.route("/")
def index():

    # check is name variable is passed in URL
    if "name" in request.args:
        name = request.args["name"]  # note square brackets
    else:
        name="World"



    # render the web page    
    htmlPage = render_template("index.html", placeholder=name)
    return htmlPage

