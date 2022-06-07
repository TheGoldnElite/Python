from flask_app import app
from flask import render_template,request,redirect,session,flash
from flask_app.models.project import Project
from flask_app.models.user import User

@app.route('/project/new')
def newproject():
    return render_template("addpost.html")


@app.route('/create',methods=['POST'])
def createproject():
    if Project.validateproject(request.form):
        data= {
            'description':request.form['description'],
            'name':request.form['name'],
            'dimensions':request.form['dimensions'],
            'instructions':request.form['instructions'],
            'user_id':session['user_id']
        }
        Project.save_show(data)
    else:
        return redirect('/project/new')

    return redirect('/dashboard')


