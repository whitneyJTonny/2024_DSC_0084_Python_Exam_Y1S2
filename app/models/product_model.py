from flask import Flask
from app.extensions import db
from datetime import datetime #importing the necessary libariries that are going to be used

class Product():
    __tablename__ = "Product"
    id = db.Column(db.Integer, Primary_Key = True, nullable = False)
    name = db.Column(db.String(255), nullable = False)
    brand = db.Column(db.String(255), nullable = False)
    price = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.datetime(255), default = datetime.now)
    update_at = db.Column(db.datetime(255), default = datetime.now)
    
    
    def __init__(self, id, name, brand, price, description, created_at, updated_at):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.description = description
        self.created_at = created_at
        self.update_at = updated_at