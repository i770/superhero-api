from extensions import db
from models.heropower import HeroPower  # Explicit import
from sqlalchemy.orm import validates

class Power(db.Model):
    __tablename__ = 'powers'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('models.heropower.HeroPower', backref='power', cascade='all, delete-orphan')

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return description

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
