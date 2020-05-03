from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "Fill the form instead <a href='/'> click here </a>"
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)
