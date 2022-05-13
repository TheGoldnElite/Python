from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User

    
# gets all the burgers and returns them in a list of burger objects .
@app.route('/user')
def user():
	return render_template('results.html',users=User.get_all())
        


# burgers.py...
from flask_app.models.user import User
# gets all the burgers and returns them in a list of burger objects .
@app.route('/create/user',methods=['POST'])
def create_user():
	data = {
        "id" : request.form['name'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "created_at" : request.form['created_at'],
        "updated_at":request.form['updated_at']
	}
	User.save(data)
	return redirect('/user')






@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_user.html",user=User.get_one(data))


@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')