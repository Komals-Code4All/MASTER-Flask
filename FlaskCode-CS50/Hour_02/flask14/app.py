from flask import Flask, render_template, request

''' Build a simple sports club registration app '''


app = Flask(__name__)   # tell Flask to make this code a web application

# define allowed values for server-side validation
SPORTS = ["Basketball", "Football", "Frisbee",]

# creat a list to store names
REGISTERANTS = {}   
@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():

    # if not request.form.get("name") or request.form.get("sport") not in SPORTS:
    #     return render_template("failure.html")

    # get name from form, and check if entered
    name=request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")


    # get sport from form, and check if entered
    sport=request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")


    REGISTERANTS[name] = sport  # adding a (unique) key:value pair

    return render_template("success.html")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTERANTS)