from flask_app import app
from flask import Flask,render_template,request,redirect

    #import

@app.route("/oneSchool/<int:id>")
def one_school_with_witchers(id):
    data = {
        'id':id
    }
    school=School.get_school_with_witchers(data)

    return render_template("one_school.html",one_school_from_controller=school)

@app.route("/")
def index():
    witchers= Witcher.get_all_witchers()
    return render_template("index.html", template_witchers=witchers)

@app.route("/create",method=['POST'])
def create_witcher():
    data ={
        'name': request_form['name_from_form']
        ''
    }





    @classmethod
    def get_all_witchers(cls):
        query="SELECT * FROM witchers;"

        results =connectToMySQL('witchers').query_db(query)