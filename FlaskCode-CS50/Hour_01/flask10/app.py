
from flask import Flask, render_template, request

''' render_templates automatically looks for html files in the templates file'''
''' request.args reads the arguements passed into the URL '''

''' 
This version uses html form to pass query data to the web page
'''

'''' Handle GET and POST from single routing 
    don't show URL in browsee bar
'''

app = Flask(__name__)   # tell Flask to make this code a web application


@app.route("/", methods = ["GET", "POST"])
def index():

    if request.method == "POST":
        name=request.form.get("name") # removed default 'World'     
        return render_template("greet.html", name=name)
    else: # method is GET, send default index.html page
        return render_template("index.html")

