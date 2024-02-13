from flask import Flask, render_template, flash
from jinja2 import Environment, PackageLoader, StrictUndefined
from forms import RegisterForm, LoginForm, AddGame

app = Flask(__name__)
app.secret_key = "SuperDuperSecretKey"
app.jinja_env.undefined = StrictUndefined


@app.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm()
    return render_template("home.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)

@app.route("/user")
def user():
    pass

if __name__ == "__main__":
    app.run(debug = True)