from flask import Flask, render_template, request, redirect, url_for
import requests

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>hi<p>"

@app.route("/welcome")
def welcome():
    return "<p>welcome<p>"

@app.route("/welcome/home")
def home():
    return "<p>welcome home<p>"

@app.route("/welcome/back")
def back():
    return "<p>welcome back<p>"

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
    url = "https://api.openweathermap.org/data/2.5/weather?&appid=60aa068482d6ddc251ae5f53570ac5fb&units=metric&q="+city
    response = requests.get(url).json()
    temperature=response["main"]["temp"]
    return render_template("displayWeather.html", city=city,response=response,temperature=temperature)

if __name__=="__main__":
    app.run(debug=True)