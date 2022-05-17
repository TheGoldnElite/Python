from flask_app import app
from flask import render_template,redirect,request
from flask_app.models import dojo
from flask_app.models.ninja import Ninja


@app.route('/ninjas')
def ninjas():
    all_dojo=dojo.Dojo.get_all()
    return render_template('new_ninja.html', all_dojo=all_dojo)


@app.route('/create/ninja', methods=['POST'])
def ninja():
    data = {
        "dojo_id":request.form['dojo_id'],
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "age":request.form['age']
    }
    Ninja.save(data)
    return redirect('/dojos')

