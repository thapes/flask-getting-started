import json

def load_db():
    with open("flashcards_db.json") as f:
        return json.load(f)

def save_db():
    with open("flashcards_db.json", 'W') as f:
        return json.dumb(db, f)


db = load_db()