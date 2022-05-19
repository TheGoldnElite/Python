from flask_app import app
from flask import render_template,redirect,request,flash,session
from flask_app.models.dog import Dog
from flask_app.models.user import User

#=======================
# Create Dog Routes
#=======================

@app.route("/new_dog")
def new_dog():
    if "user_id" not in session:
        flash("Please register or login before entering out site")
        return redirect("/")
    data={
        "user_id":session['user_id']
    }
    logged_user=User.get_by_id(data)
    return render_template("new_dog.html",user=logged_user)



@app.route("/create_dog",methods=["POST"])
def create_dog():
    if not Dog.validate_dog(request.form):
        return redirect("/new_dog")

    data={
        "name":request.form['name'],
        "breed":request.form['breed'],
        "age":request.form['age'],
        "user_id":session['user_id']
    }
    Dog.save_dog(data)

    return redirect("/dashboard")






















