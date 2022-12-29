from flask import Flask, render_template, request, redirect, url_for

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

@app.route("/dashboard/<city>")
def dashboard(city):
    return render_template("displayWeather.html", city=city)

@app.route("/weather",methods=["POST", "GET"])
def weather():
    if request.method == "POST":
        temp=request.form["city"]
        return redirect(url_for("dashboard",city=temp))
    else:
        temp=request.args.get("city")
        return render_template("chooseCity.html")


if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)