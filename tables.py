from __init__ import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config_local import (sql_url)
from datetime import datetime
# from config import (sql_url)


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

class Calendar_table(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    event_date = db.Column(db.DateTime, nullable=False)
    event_time = db.Column(db.DateTime, nullable=False)
    event_hour = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Calendar_table %r>' % self.event_id