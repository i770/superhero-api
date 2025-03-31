from app import db, app  # Import the app instance
from flask_migrate import Migrate  # Import Flask-Migrate

migrate = Migrate(app, db)  # Initialize Flask-Migrate

if __name__ == '__main__':
    from flask import Flask
    app.run()
