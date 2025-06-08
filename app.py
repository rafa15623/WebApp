from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, NobelWinner
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nobel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/random_winners")
def random_winners():
    winners = NobelWinner.query.all()
    sampled = random.sample(winners, 5)
    return jsonify([{"name": w.name, "year": w.year, "category": w.category, "country": w.country} for w in sampled])

@app.route("/api/country_counts")
def country_counts():
    results = db.session.query(NobelWinner.country, db.func.count(NobelWinner.id)).group_by(NobelWinner.country).all()
    return jsonify({"labels": [r[0] for r in results], "values": [r[1] for r in results]})

@app.route("/api/categories_by_country")
def categories_by_country():
    results = db.session.query(
        NobelWinner.country,
        NobelWinner.category,
        db.func.count()
    ).group_by(NobelWinner.country, NobelWinner.category).all()

    data = {}
    for country, category, count in results:
        if not country or not category:
            continue  # salta registros incompletos
        if country not in data:
            data[country] = {}
        data[country][category] = count

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
