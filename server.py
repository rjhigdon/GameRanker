from flask import Flask
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)
app.secret_key = "SuperDuperSecretKey"

env = Environment(
    loader=PackageLoader("GameRanker"),
    autoescape=select_autoescape()
)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login")
def login():
    pass
