from flask_app import app
from flask import render_template,redirect,request
from models.dojo import Dojo
from models.ninja import Ninja


@app.route('/ninjas')
def ninjas():
    return render_template('new_ninjas.html',all_ninjas=Ninja.get_all())


@app.route('/ninja',methods=['POST'])
def ninja():
    data = {
        "dojo_id":request.form['dojo_id'],
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "age":request.form['age']
    }
    ninjas_id = Ninja.save(data)
    return redirect('/ninjas')