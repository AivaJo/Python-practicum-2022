from flask import Flask, render_template, request, redirect, url_for
import requests
from datetime import datetime
import matplotlib.pyplot as plt
plt.switch_backend('Agg')
import plotly.express as px 
from meteostat import Point, Daily
import pandas as pd
from openpyxl.workbook import workbook
import mpld3


app=Flask(__name__)

api_key = "60aa068482d6ddc251ae5f53570ac5fb"
units = "metric"

@app.route("/")
def hello_world():
    return render_template("layout.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/welcome/home")
def home():
    return render_template("welcomeHome.html")

@app.route("/welcome/back")
def back():
    return render_template("welcomeBack.html")

@app.route("/weather",methods=["POST", "GET"])
def weather():
    
    if request.method == "POST":
        name=request.form["city"]
        return redirect(url_for("dashboard",city=name))
    else:
        name=request.args.get("city")
        return render_template("chooseCity.html")

@app.route("/dashboard/<city>")
def dashboard(city):
    url = "https://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&units="+units+"&q="+city
    response = requests.get(url).json()
    temperature=response["main"]["temp"]
    return render_template("displayWeather.html", city=city,response=response,temperature=temperature)

@app.route("/weather_history",methods=["POST", "GET"])
def history():
   
    if request.method == "POST":

        name2=request.form["city2"]
        city2=name2

        url2 = "http://api.openweathermap.org/geo/1.0/direct?q="+city2+"&limit=1&appid="+api_key
        response2 = requests.get(url2).json()
        lat=response2[0]['lat']
        lon=response2[0]['lon']

        end=datetime.today()
        start=pd.to_datetime(end)-pd.DateOffset(years=1)
        city_point=Point(lat,lon)
        data=Daily(city_point,start,end)
        data=data.fetch()

        df=pd.DataFrame(data, columns=['tavg', 'tmin', 'tmax'])
        df = df.rename(columns = {"tavg":"average","tmin":"min","tmax":"max"})
        df.to_excel("history/excelis.xlsx", sheet_name=city2+"_history")

        fig=px.line(df, title="temperature history "+city2)
        fig.update_xaxes(title_text='Dates')
        fig.update_yaxes(title_text='Temperature')
        fig.write_image("static/fig1.png")
        fig.write_image("static/fig1.pdf")
        
        return render_template("history.html",city2=city2)
    else:
        name2=request.args.get("city2")
        return render_template("history.html")
    

if __name__=="__main__":
    app.run(debug=True)