from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Many-to-Many association table
user_plants = db.Table('user_plants',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('plant_id', db.Integer, db.ForeignKey('plant.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True, nullable=False)
    saved_plants = db.relationship('Plant', secondary=user_plants, backref=db.backref('users', lazy='dynamic'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String(120), nullable=False)
    scientific_name = db.Column(db.String(120), nullable=False, unique=True)
    family = db.Column(db.String(120))
    genus = db.Column(db.String(120))
    year_discovered = db.Column(db.Integer)
    flower_color = db.Column(db.String(120))
    flower_conspicuous = db.Column(db.Boolean)
    foliage_texture = db.Column(db.String(120))
    foliage_color = db.Column(db.String(120))
    growth_rate = db.Column(db.String(120))
    growth_habit = db.Column(db.String(120))
    growth_form = db.Column(db.String(120))
    edible_part = db.Column(db.String(120))
    edible = db.Column(db.Boolean)
    images = db.relationship('PlantImage', backref='plant', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class PlantImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.id'), nullable=False)
 

