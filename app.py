from flask import Flask, render_template
from data import kontakter

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/meny")
def meny():
    return render_template("meny.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html", epost = kontakter["epost"], nummer = kontakter["nummer"])

@app.route("/varer")
def varer():
    return render_template("varer.html")

if __name__ == "__main__":
    app.run()