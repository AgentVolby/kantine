from flask import Flask, render_template
from data import kontakter, bakevarer, drikker, menydag
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/meny")
def meny():
    now = datetime.now()
    liste = now.weekday()
    if liste >= 5:
        liste = 0

    return render_template("meny.html", menyliste = menydag, dag = datetime.now())

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html", epost = kontakter["epost"], nummer = kontakter["nummer"])

@app.route("/varer")
def varer():
    return render_template("varer.html", bake = bakevarer, drikke = drikker)

if __name__ == "__main__":
    app.run()