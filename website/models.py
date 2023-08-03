from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Product (db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key
    product_name = db.Column(db.String(255))
    abcam_id = db.Column(db.String(255))
    img_path = db.Column(db.String(255)) 
    description = db.Column(db.String(10000))
    abcam_link = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # primary key
    email = db.Column(db.String(150), unique=True) # unique email
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))