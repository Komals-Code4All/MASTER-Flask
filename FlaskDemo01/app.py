'''
Flask with simple 3-page website

Run the Flask server using "flask run".
the ctr-click th eip address is shows in the VSCode terminal, e.g. 172.0.0.1:5000


'''
from flask import Flask 
from flask import render_template   # render an HTML template

app = Flask(__name__)


@app.route("/")
def indexPage():
    return render_template('index.html')

@app.route("/about")
def aboutPage():
    return render_template('about.html')


@app.route("/contact")
def contactPage():
    return render_template('contact.html')

