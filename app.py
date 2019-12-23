from flask import Flask, render_template, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from config_local import sql_user, sql_pass
# from datetime import 
# from config import (sql_url)

app = Flask(__name__)

# SQL Connection
# engine = create_engine(f'{sql_url}')
engine = create_engine(f'mysql://{sql_user}:{sql_pass}@ofcmikjy9x4lroa2.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/o5hjwzcvjuw3utaz')

Base = automap_base()
Base.prepare(engine, reflect=True)



@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/home')
def home():
    
    return render_template('index.html')

@app.route('/bio')
def bio():
    
    return render_template('bio.html')

@app.route('/services')
def services():
    
    return render_template('services.html')

@app.route('/contact')
def contact():
    
    return render_template('contact.html')

@app.route('/contact', methods=['POST'])
def contact_post():
    first_name = request.form['firstName']
    last_name = request.form['lastName']
    company_name = request.form['companyName']
    email_address = request.form['emailAddress']
    apt_date = request.form['aptDate']
    apt_time = request.form['aptTime']
    work_desc = request.form['workDesc']

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)