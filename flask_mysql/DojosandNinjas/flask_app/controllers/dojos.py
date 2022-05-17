from flask_app import app
from flask import redirect,render_template,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    all_dojos=Dojo.get_all()
    return render_template('dojo.html', all_dojos=all_dojos)


@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    data={
        "name":request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data={
        "id":id
    }
    return render_template('show_dojo.html',dojo=Dojo.get_dojos(data))