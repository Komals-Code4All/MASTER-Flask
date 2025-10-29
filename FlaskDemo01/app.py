'''
Flask with simple 3-page website

    This program is the mian program that Flask will look for to route url requests 

    Run the Flask server using "flask run".
    then ctr-click the ip address is showns, e.g. 172.0.0.1:5000

    Use ctrl-c to end the Flask server

'''

from flask import Flask 
from flask import render_template   # render an HTML template


app = Flask(__name__)

# default routing for url '127.0.0.1:5000/'
@app.route("/")
def indexPage():
    return render_template('index.html')

# routing for url '127.0.0.1:5000/about'
@app.route("/about")
def aboutPage():
    return render_template('about.html')

# routing for url '127.0.0.1:5000/contact'
@app.route("/contact")
def contactPage():
    return render_template('contact.html')

