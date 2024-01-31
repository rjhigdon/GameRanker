from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(25), unique = True, nullable = False)
    password = db.Column(db.String(25), nullable = False)
    email = db.COlumn(db.String(50), nullable = False)
    logged_in = db.Column(db.Boolean, nullable = False)
    rating = db.Column(db.Integer, nullable = True)    

class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(50), nullable = False)
    genre = db.Column(db.String(50), nullable = False)
    vgConsole = db.Column(db.String(50), nullable = False)
    

class Rating(db.Model):
    pass