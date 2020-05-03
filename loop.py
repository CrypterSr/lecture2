from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Hydrogen", "Helium", "lithium", "berilium", "boron", "carbon", "nitrogen", "oxygen", "flourine", "neon"]
    for name in range(len(names)):
        names[name] = names[name].capitalize()
    return render_template("looplist.html", names=names)
