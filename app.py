from flask import Flask, render_template, jsonify, request
from sqlalchemy import create_engine
from config_local import sql_user, sql_pass
# from config import (sql_url)

app = Flask(__name__)

engine = create_engine(f'mysql://{sql_user}:{sql_pass}@ofcmikjy9x4lroa2.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/o5hjwzcvjuw3utaz')
# engine = create_engine(f'{sql_url}')

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/home")
def home():
    
    return render_template("index.html")

@app.route("/bio")
def bio():
    
    return render_template("bio.html")

@app.route("/services")
def services():
    
    return render_template("services.html")

@app.route("/contact")
def contact():
    
    return render_template("contact.html")

@app.route("/submit")
def submit():
    
    return 'Button Was Clicked'

if __name__ == "__main__":
    app.run(debug=True)