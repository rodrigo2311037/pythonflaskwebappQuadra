from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class FoodStall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(1000))
    latitude = db.Column(db.Integer)  # Localizacion 
    longitude = db.Column(db.Integer)
    image_url = db.Column(db.String(500))  # URL de la foto
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Relación con el usuario que sube el puesto
    reviews = db.relationship('Review', backref='related_food_stall', lazy=True)  # Relación con las reseñas

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)  # Calificación (de 1 a 5)
    comment = db.Column(db.String(500))  # Comentario
    # Foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Relación con el usuario que califica
    foodstall_id = db.Column(db.Integer, db.ForeignKey('food_stall.id'))  # Relación con el puesto de comida
    # Relaciones
    user = db.relationship('User', backref='reviews')  # Relación con la clase User para acceder al autor de la reseña
    food_stall = db.relationship('FoodStall', backref='related_reviews')

