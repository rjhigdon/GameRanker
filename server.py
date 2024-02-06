from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    pass

@app.route("/login")
def login():
    pass

@app.route("/register")
def register():
    pass

