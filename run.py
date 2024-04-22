import os
from flask import Flask, render_template # render_template to import files into the website


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")



if __name__ == "__main__":  # is the name of the default module in Python.
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")), #"5000", which is a common port used by Flask.
        debug = True #because that will allow us to debug our code much easier during the development stage. but it has to be set false later.
    )