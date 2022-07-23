from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/scrape")
def scrape():
    data = scrape_mars.scrape()

    return 
