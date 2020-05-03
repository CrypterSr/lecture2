from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    date = datetime.datetime.now()
    print(date.day)
    today = date.month == 5 and date.day == 3
    return render_template("date.html", date=today)