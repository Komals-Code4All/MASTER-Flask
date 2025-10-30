'''  Flask controlling & routing program      '''

from flask import  Flask, render_template
import os

app = Flask(__name__) 

@app.route("/")
def indexPage():
    return render_template("index.html")

@app.route("/about")
def aboutPage():
    return render_template("about.html")

@app.route("/contact")
def contactPage():
    return render_template("contact.html")

@app.route("/custqry")
def custqryPage():
    os.system('python getCustData.py')
    return render_template("custqry.html")

