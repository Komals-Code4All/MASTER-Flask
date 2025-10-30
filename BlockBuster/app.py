''' Main controlling app for the Blockbuster Store '''

# imports
from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)

# turn on session cookies, delete when session ends
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Home Page-------------------------------------------------------------------
@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html", userid=session.get("userid"))


# Products Page-------------------------------------------------------------------
@app.route("/products", methods=["POST", "GET"])
def products():
    # connect to database and get list of films
    return render_template("products.html", userid=session.get("userid"))




# Log-in page -------------------------------------------------------------------
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["userid"] = request.form.get("userid")
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
