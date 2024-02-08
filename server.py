from flask import Flask
from jinja2 import Environment, PackageLoader, select_autoescape, render_template

app = Flask(__name__)
app.secret_key = "SuperDuperSecretKey"

env = Environment(
    loader=PackageLoader("yourapp"),
    autoescape=select_autoescape()
)

@app.route("/")
def homepage():
    pass

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    pass

