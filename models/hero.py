from extensions import db
from models.heropower import HeroPower

class Hero(db.Model):
    __tablename__ = 'heroes'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('models.heropower.HeroPower', backref='hero', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name,
            'powers': [hp.power.to_dict() for hp in self.hero_powers]
        }
