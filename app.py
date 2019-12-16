from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)