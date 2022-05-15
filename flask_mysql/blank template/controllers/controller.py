form flask_app import app
from flask import render_template,request
from flask_app.model_name import"class_name"

@app.route("/")
def index():
    print("test")
    return render_template("index.html")
    #when have form with action need 2 route 1 form(need to render) 1 reroute(action that occurs)
