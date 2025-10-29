
from flask import Flask

app = Flask(__name__)   # tell Flask to make this code a web application

# decorators - wrap a function inside another function
@app.route("/")
def index():
    return "<!DOCTYPE html><html><body><h1>Hello, World!</h1></body></html>"  

