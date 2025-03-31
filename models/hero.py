from app import db

class Hero(db.Model):
    __tablename__ = 'hero'
    __table_args__ = {'extend_existing': True}  # Allow redefining the table

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Hero {self.name} - {self.super_name}>'
