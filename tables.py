from __init__ import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from config_local import sql_user, sql_pass
from datetime import datetime
from config import (sql_url)


# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{sql_user}:{sql_pass}@ofcmikjy9x4lroa2.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/o5hjwzcvjuw3utaz'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'{sql_url}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Customer_site_dump(db.Model):
    customer_key = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(20), nullable=True)
    company_name = db.Column(db.String(20), nullable=True)
    apt_date = db.Column(db.DateTime, nullable=True) 
    apt_time = db.Column(db.DateTime, nullable=True) 
    service_desc = db.Column(db.String(80), nullable=True)
    email_address = db.Column(db.String(80), nullable=True, unique=True)
    ts = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Customer_site_dump %r>' % self.email_address