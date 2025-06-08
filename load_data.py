import json
from app import app
from models import db, NobelWinner

with app.app_context():
    db.drop_all()
    db.create_all()

    with open('nobel_winners_clean.json') as f:
        data = json.load(f)
        for item in data:
            winner = NobelWinner(
                name=item.get("name", ""),
                year=item.get("year", 0),
                category=item.get("category", ""),
                country=item.get("country", "")
            )
            db.session.add(winner)
        db.session.commit()
