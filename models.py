from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class NobelWinner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    year = db.Column(db.Integer)
    category = db.Column(db.String(64))
    country = db.Column(db.String(64))
