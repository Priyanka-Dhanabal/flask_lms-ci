import os
import json
from flask import Flask, render_template, request, flash 
# render_template to import files into the website
# request library will handle things like finding out what methos was used and it will contain the form object when we have posted it.
# flash : we want to display a non-permanent message to the user, something that only stay on screen until we refresh the page, or go to a different one.
# These are called 'flashed messages' in Flask.  we need to create a secret key, because Flask cryptographically signs all of the messages for security purposes.

if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data: # Python open the JSON file in order to read it. This is called a 'with' block.
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
       data = json.load(json_data)
       for obj in data:
         if obj["url"] == member_name:
            member = obj

    return render_template("member.html", member=member) 
    # This first 'member' is the variable name being passed through into our html file.
    # The second 'member' is the member object we created above on line 24.


@app.route("/contact", methods=["GET", "POST"]) #we need to explicitly state that our route can accept those methods. by default it has only get method.
def contact():
    if request.method =="POST":
        # print(request.form)
        # print(request.form.get("name"))
        # print(request.form["email"])
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")



if __name__ == "__main__":  # is the name of the default module in Python.
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")), #"5000", which is a common port used by Flask.
        debug = True #because that will allow us to debug our code much easier during the development stage. but it has to be set false later.
    )