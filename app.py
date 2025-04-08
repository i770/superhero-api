from flask import Flask, request, jsonify
from extensions import db
from flask_migrate import Migrate
from models import Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Import and register your routes here
from routes import *

if __name__ == '__main__':
    app.run(port=5555, debug=True)
