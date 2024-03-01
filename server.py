from flask import Flask, render_template, flash, redirect
from jinja2 import Environment, PackageLoader, StrictUndefined
from forms import RegisterForm, LoginForm, AddGame
from model import User, Game, db, connect_to_db
from flask_login import LoginManager, login_required

app = Flask(__name__)
app.secret_key = "SuperDuperSecretKey"
app.jinja_env.undefined = StrictUndefined

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/", methods=["GET", "POST"])
def home():
    form = LoginForm()
    return render_template("home.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = User(username = form.username.data, password = form.password.data)
    if form.validate_on_submit:
        login(user)
        flash(f"user: {user.username} logged in")
        return redirect("/user")
    return render_template("login.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    new_user = User(username = form.username.data, password = form.password.data)
    if form.validate_on_submit():
        db.session.add(new_user)
        db.session.commit()
        flash(f"new user {new_user.username} created successfully")
        return redirect("login.html")
    return render_template("register.html", form=form)

@app.route("/user") 
@login_required
def user():
    pass

if __name__ == "__main__":
    app.run(debug = True)
    login_manager.init_app(app)