from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from bs4 import BeautifulSoup
import requests
app.config['SECRET_KEY']='fbfcba0ab308bfd68656b2409bf1fb8b'



@app.route('/', methods=['GET', 'POST'])
def home():
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    city = "Pune"
    api_key = '&APPID=be530b1292724ccf99abb82222a63543'
    comp = base_url + city + api_key
    res = requests.get(comp).json()
    weather = {
        'city': city,
        'description':res["weather"][0]["description"],
        'temp': res["main"]["temp"],
        'humidity':res["main"]["humidity"],
        'pressure':res["main"]["pressure"]
    }
    if request.method == 'POST':
        comp = base_url + request.form["find"].capitalize() + api_key
        res = requests.get(comp).json()
        if res["cod"]!="404":
            weather["city"]=request.form["find"].capitalize()
            weather["temp"]=res["main"]["temp"]
            weather["humidity"]=res["main"]["humidity"]
            weather["pressure"]=res["main"]["pressure"]
            weather["description"]=res["weather"][0]["description"]
        else:
            flash("City not found try again","danger")
    title='Weather-forecast'
    return render_template('index.html', title=title, weather=weather)