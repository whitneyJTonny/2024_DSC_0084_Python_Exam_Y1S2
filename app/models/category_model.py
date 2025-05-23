from flask import Flask
from app.extensions import db
from datetime import datetime

class Category():
    __table__ = "Category"
    id = db.Column(db.Integer, Primary_Key = True, nullable = True)
    name = db.Column(db.String(50), nullable = False)
    expiry_date = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.datetime(255), default = datetime.now)
    update_at = db.Column(db.datetime(255), default = datetime.now)
    
        
    def __init__(self, id, name, expiry_date, description, created_at, updated_at):
        self.id = id
        self.name = name
        self.expiry_date = expiry_date
        self.description = description
        self.created_at = created_at
        self.update_at = updated_at