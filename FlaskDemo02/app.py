""" 
To run this code:    flask run

                flask --app flaskApp.py run
Then follow the IP address as a web browser

"""

from flask import Flask 
from flask import render_template   # render an HTML template
from flask import request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def indexPage():
    return render_template('index.html')

@app.route("/about", methods=["GET","POST"])
def aboutPage():
    return render_template('about.html')


@app.route("/contact", methods=["GET" ,"POST"])
def contactPage():
    return render_template('contact.html')

