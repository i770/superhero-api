from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Set the database URI
db = SQLAlchemy(app)

class HeroBase(db.Model):  # Renamed from Hero to HeroBase
    id = db.Column(db.Integer, primary_key=True)

# Other code...
