import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_googlemaps import GoogleMaps


load_dotenv()
app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = "AIzaSyBoiMngvBd_A7ORI7ouP5zi8BhRsPL1vFY"
GoogleMaps(app)
    

@app.route('/')
def index():
    return render_template('index.html', title="Group Water", url=os.getenv("URL"))

