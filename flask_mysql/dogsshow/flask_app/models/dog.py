from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
class Dog:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.breed=data['breed']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        
        self.owner={}
        

    @staticmethod
    def validate_dog(form_data):
        is_valid=True
        if len(form_data['name']) < 2:
            flash("Name must be at least 2 characters long!")
            is_valid=False
        if len(form_data['breed']) < 2:
            flash("Breed must be at least 2 characters long! ")
            is_valid=False
        if form_data['age']=="":
            flash("Please enter an age")
            is_valid=False
        elif int(form_data['age']) < 2:
            flash("Age must be older than 2")
            is_valid=False
        return is_valid

    @classmethod
    def save_dog(cls,data):
        query = "INSERT INTO dogs (name,breed,age,user_id,created_at,updated_at) VALUES (%(name)s,%(breed)s,%(age)s,%(user_id)s,NOW(),NOW()"
        results = connectToMySQL("dogshow_schema").query_db(query,data)
        return results

    @classmethod
    def get_all_dogs(cls):
        query="SELECT * FROM LEFT JOIN users ON users.id=dogs.user_id;"
        results = connectToMySQL("dogshow_schema").query_db(query)
        
        all_dogs=[]
        
        for row in results:
            dog=cls(row)

            user_data={
                "id":row['id'],
                "name":row['name'],
                "breed":row['breed'],
                "age":row['age'],
                "created_at":row['created_at'],
                "updated_at":row['updated_at'],
            }

            dog.owner=user.User(user_data)
            all_dogs.append(dog)
        return all_dogs











