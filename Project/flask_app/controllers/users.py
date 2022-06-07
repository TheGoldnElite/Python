from flask_app import app
from flask import render_template,redirect,request,flash,session
from flask_app.models.user import User
from flask_app.models.project import Project
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/users/register',methods=['POST'])
def register_user():
    if User.validate_user(request.form):
        data={
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email':request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        User.create_user(data)
    else:  
        print("is not valid")
    return redirect ('/')


@app.route('/users/login',methods=['POST'])
def login_user():
    users = User.get_user_by_email(request.form)

    if len(users) != 1:
        flash("Incorrect email addresss")
        return redirect ('/')
    user=users[0]
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("Incorrect password")
        return redirect('/')

    session['user_id']=user.id
    session['email']=user.email
    session['first_name']=user.first_name
    session['last_name']=user.last_name
    
    return redirect('/dashboard')
    
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("You must be logged in to view this website")
        return redirect('/')

    data={
        "user_id":session['user_id']
    }
    user=User.get_id(data)

    #get all shows for dashboard
    # all_show=Show.getshow()

    return render_template('dashboard.html',user=user)
    # ,all_show=all_show)
    


@app.route('/logout')
def logout():
    session.clear()
    flash("Successfully logged out")
    return redirect ('/')