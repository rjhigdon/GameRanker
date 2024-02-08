from flask import Flask, render_template, flash
from jinja2 import Environment, PackageLoader, StrictUndefined

app = Flask(__name__)
app.secret_key = "SuperDuperSecretKey"
app.jinja_env.undefined = StrictUndefined()


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return "GameRanker login"

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug = True)