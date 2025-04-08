from extensions import db
from app import app
from models.hero import Hero
from models.power import Power
from models.heropower import HeroPower

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Seed heroes
        heroes = [
            Hero(name="Kamala Khan", super_name="Ms. Marvel"),
            Hero(name="Doreen Green", super_name="Squirrel Girl"),
            Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        ]
        db.session.bulk_save_objects(heroes)

        # Seed powers
        powers = [
            Power(
                name="super strength",
                description="gives the wielder super-human strengths"
            ),
            Power(
                name="flight",
                description="gives the wielder the ability to fly through the skies at supersonic speed"
            ),
            Power(
                name="super speed",
                description="allows the wielder to move at incredible velocity"
            )
        ]
        db.session.bulk_save_objects(powers)

        # Seed hero_powers
        hero_powers = [
            HeroPower(hero_id=1, power_id=2, strength="Strong"),
            HeroPower(hero_id=2, power_id=1, strength="Average"),
            HeroPower(hero_id=3, power_id=3, strength="Weak")
        ]
        db.session.bulk_save_objects(hero_powers)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
