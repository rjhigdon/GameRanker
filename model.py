import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(25), unique = True, nullable = False)
    password = db.Column(db.String(25), nullable = False)
    
    game = db.relationship("Game", backref = "user", lazy = True)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<user: {self.username}"

class Game(db.Model):
    
    __tablename__ = "games"
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(50), nullable = False)
    genre = db.Column(db.String(50), nullable = False)
    vg_console = db.Column(db.String(50), nullable = True)
    release_yr = db.Column(db.Integer, nullable = True)
    play_yr = db.Column(db.Integer, nullable = True)
    description = db.Column(db.String(250), nullable = True) 
    rating = db.Column(db.Integer, nullable = False) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __init__(self, title, genre, vg_console, release_yr, play_yr, description, rating):
        self.title = title
        self.genre = genre
        self.vg_console = vg_console
        self.release_yr = release_yr
        self.play_yr = play_yr
        self.description = description
        self.rating = rating

def connect_to_db(app):
    try:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["POSTGRES_URI"]
    except KeyError:
        print("provide POSTGRES_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    
if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    print("Connected to db...")
    
    with app.app_context():
        db.create_all()
        