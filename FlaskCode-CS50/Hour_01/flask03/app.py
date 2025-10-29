
from flask import Flask, render_template

''' render_templates automatically looks for html files in the templates file'''

app = Flask(__name__)   # tell Flask to make this code a web application

# decorators - wrap a function inside another function
@app.route("/")
def index():
    htmlPage = render_template("index.html")
    return htmlPage

