from __init__ import app
from flask import Flask, render_template, jsonify, request
from tables import Customer_site_dump, db
import datetime as dt


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
    data = [{ 'message' : ''}]
    return render_template('contact.html', data=data)

@app.route('/contact', methods=['POST'])
def contact_post():
    form = request.form
    first_name = form['firstName']
    last_name = form['lastName']
    company_name = form['companyName']
    email_address = form['emailAddress']
    apt_date = form['aptDate']
    apt_time = form['aptTime']
    service_desc = form['serviceDesc']
    ts = dt.datetime.now()
    submitted_info = Customer_site_dump(first_name=first_name, last_name=last_name, company_name=company_name, apt_date=apt_date, apt_time=apt_time, service_desc=service_desc, email_address=email_address, ts=ts)
    data = [{ 'message' : f'Thank you for your interest {first_name}! Someone from our team will contact you shortly.'}]

    db.session.add(submitted_info)
    db.session.commit()

    return render_template('contact.html', form=form, data=data)

if __name__ == '__main__':
    app.run(debug=True)