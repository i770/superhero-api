from flask import Flask
from flask_migrate import Migrate
from app import db  # Import the db instance from your app
from models.hero import Hero  # Import the Hero model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Set the database URI
migrate = Migrate(app, db)  # Initialize Flask-Migrate

@app.route('/')
def home():
    return "Welcome to the Flask Application!"

@app.route('/heroes')
def get_heroes():
    # Fetch all heroes from the database
    heroes = Hero.query.all()
    return {"heroes": [hero.name for hero in heroes]}  # Return the list of hero names

if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)  # Initialize the db with the app context
        db.create_all()  # Create tables if they don't exist
        migrate.init_app(app, db)  # Initialize migrations
    app.run(debug=True, port=5015)  # Run on a different port
