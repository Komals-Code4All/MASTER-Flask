
from flask import Flask, render_template, request

''' render_templates automatically looks for html files in the templates file'''
''' request.args reads the arguements passed into the URL '''

''' 
Passing a query to the server URL   
    http://127.0.0.1:5000/?name=komal 
    
    http://127.0.0.1:5000/
    without ?name=""   defaults to World
'''


app = Flask(__name__)   # tell Flask to make this code a web application

# decorators - wrap a function inside another function
@app.route("/")
def index():

    # args is a dictionary - get the key:value pair for args key=name, default="World"
    name = request.args.get("name", "World")          # note round brackets
 
    # render the web page    
    # use the key:value names as 'placeholder' names
    htmlPage = render_template("index.html", name=name)
    return htmlPage

