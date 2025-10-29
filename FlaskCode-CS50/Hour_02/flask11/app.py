from flask import Flask, render_template, request

''' Build a simple sports club registration app '''


app = Flask(__name__)   # tell Flask to make this code a web application

# define allowed values for server-side validation
SPORTS = ["Basketball", "Football", "Frisbee",]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or request.form.get("sport") not in SPORTS:
        return render_template("failure.html")
    return render_template("success.html")

