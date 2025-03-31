from flask import Flask
from flask_migrate import Migrate
from app import db  # Import the db instance from your app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Set the database URI
migrate = Migrate(app, db)  # Initialize Flask-Migrate

@app.route('/')
def home():
    return "Welcome to the Flask Application!"

@app.route('/heroes')
def get_heroes():
    return {"heroes": []}  # Placeholder for the actual implementation

if __name__ == '__main__':
    with app.app_context():
        db.init_app(app)  # Initialize the db with the app context
        db.create_all()  # Create tables if they don't exist
        migrate.init_app(app, db)  # Initialize migrations
    app.run(debug=True, port=5008)  # Run on a different port
