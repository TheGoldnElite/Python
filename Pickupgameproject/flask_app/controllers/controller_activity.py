from flask_app import app
from flask import render_template,redirect,request,flash,session
from flask_app.models.user import User
from flask_app.models.activity import Activity
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/pickup/add')
def add_activity():
    if 'user_id' not in session:
        flash("You must be logged in to view this website")
        return redirect('/')
    
    data={
        "user_id":session['user_id']
    }
    user=User.get_id(data)
    
    return render_template("addactivity.html",user=user)

@app.route('/create',methods=['POST'])
def create():
    if Activity.validateactivities(request.form):
        data= {
            'event_name':request.form['event_name'],
            'location':request.form['location'],
            'description':request.form['description'],
            'date':request.form['date'],
            'members':request.form['members'],
            # 'time':request.form['time'],
            'user_id':session['user_id']
        }
        Activity.save_activities(data)
    else:
        return redirect('/pickup/add')

    return redirect('/dashboard')

@app.route('/edit/<int:activity_id>')
def edit(activity_id):
    if 'user_id' not in session:
        flash("You must be logged in to view this website")
        return redirect('/')
    
    data={
        "user_id":session['user_id']
    }
    user=User.get_id(data)
    data={
        "activity_id":activity_id
    }
    activity=Activity.activity_get_one(data)
    return render_template("edit.html",activity=activity,user=user)




@app.route("/update/<int:activity_id>",methods=['POST'])
def updatepage(activity_id):
    if Activity.validateactivities(request.form):
        data={
            'event_name': request.form['event_name'],
            'location': request.form['location'],
            'description': request.form['description'],
            'date': request.form['date'],
            'members': request.form['members'],
            # 'time': request.form['time'],
            'activity_id': activity_id
        }
        
    else:  
        return redirect (f"/edit/{activity_id}")
    Activity.updatepage(data)
    

    return redirect('/dashboard')

@app.route('/pickup/<int:activity_id>')
def onepage(activity_id):
    if 'user_id' not in session:
        flash("You must be logged in to view this website")
        return redirect('/')
    
    data={
        "user_id":session['user_id']
    }
    user=User.get_id(data)
    
    
    data={
        "activity_id":activity_id
    }
    activity=Activity.one_activity(data)


    return render_template("show_one.html",activity=activity, user=user)











@app.route("/delete/<int:activities_id>")
def delete(activities_id):
    data = {
        "activities_id": activities_id
    }
    Activity.delete(data)
    return redirect("/dashboard")