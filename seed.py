from app import db, app  # Import the db and app instances
from models.hero import Hero  # Import the Hero model from hero.py

# Create some initial hero records
def seed_heroes():
    # Create tables if they don't exist
    db.create_all()  # Create tables again

    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
    ]
    
    db.session.bulk_save_objects(heroes)
    db.session.commit()
    print("Heroes seeded successfully!")

if __name__ == '__main__':
    with app.app_context():
        seed_heroes()
