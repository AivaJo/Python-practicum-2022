from flask import Flask

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


if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)