from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models import user

class Recipe:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instructions=data['instructions']
        self.updated_at=data['updated_at']
        self.created_at=data['created_at']
        self.user_id=data['user_id']
        self.recipeowner = {}
        

    @staticmethod
    def validate_recipe(data):
        is_valid=True
        if (len(data['name'])) < 3:
            flash("Name must be more than three characters long")
            is_valid=False
        if (len(data['description'])) < 3:
            flash("Name must be more than three characters long")
            is_valid=False
        if (len(data['instructions'])) < 3:
            flash("Name must be more than three characters long")
            is_valid=False

        return is_valid

    @classmethod
    def save_recipe(cls,data):
        query="INSERT INTO recipes (name,description,instructions,user_id,created_at,updated_at) VALUES (%(name)s,%(description)s,%(instructions)s,%(user_id)s,NOW(),NOW());"
        results=connectToMySQL("recipe_schema").query_db(query,data)
        return results

    @classmethod
    def getrecipes(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id;"
        results=connectToMySQL("recipe_schema").query_db(query)

        all_recipes = []
        
        for row in results:
            recipe=cls(row)
            user_data = {
                "id":row['users.id'],
                "first_name":row['first_name'],
                "last_name":row['last_name'],
                "email":row['email'],
                "password":row['password'],
                "created_at":row['users.created_at'],
                "updated_at":row['users.updated_at'],
            }

            recipe.recipeowner=user.User(user_data)
            all_recipes.append(recipe)
        return all_recipes


    @classmethod
    def recipeone(cls,data):
        query="SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id =%(recipe_id)s;"
        results=connectToMySQL("recipe_schema").query_db(query,data)
        
        recipe =cls(results[0])

        user_data = {
            "id":results[0]['users.id'],
            "first_name":results[0]['first_name'],
            "last_name":results[0]['last_name'],
            "email":results[0]['email'],
            "password":results[0]['password'],
            "created_at":results[0]['users.created_at'],
            "updated_at":results[0]['users.updated_at']
        }
        recipe.recipeowner = user.User(user_data)
        return recipe

    @classmethod
    def update_recipe(cls,data):
        query="UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,updated_at=NOW(),created_at=NOW() WHERE id= %(recipe_id)s;"
        results=connectToMySQL("recipe_schema").query_db(query,data)
        return 

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id=%(recipe_id)s;"
        results=connectToMySQL("recipe_schema").query_db(query,data)
        return 