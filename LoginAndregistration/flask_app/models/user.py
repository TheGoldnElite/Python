from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class User():
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def create_user(cls,data):
        query="INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s,%(email)s,%(password)s);"
        result = connectToMySQL("loginred_schema").query_db(query,data)
        return result

    @classmethod
    def get_user_by_email(cls,data):
        query="SELECT * FROM users WHERE email = %(email)s"

        results = connectToMySQL("loginred_schema").query_db(query,data)

        users=[]
        for item in results:
            users.append(User(item))

        return users

    
    @staticmethod
    def validate_user(data):
        is_valid=True
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        
        #email must follow pattern
        if not email_regex.match(data['email']):
            is_valid= False
            flash("Please provide a valid user email")
        
        
        #email must be unique

        if len(User.get_user_by_email(data)) != 0:
            is_valid=False
            flash("Email already in use")
        
        #password must be at least 8 character
        if len(data['password']) < 8:
            is_valid=False
            flash("Password must be at least 8 characters")
        
        #confirm must match
        if data['password'] != data['confirm_password']:
            is_valid=False
            flash("Password and confirm password must match exactly")
        
        #first name must be at least 2 characters
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters")
            is_valid=False
        
        #last name must be at least 2 characters
        if len(data['last_name']) < 2:
            is_valid=False
            flash("Last name must be at least 2 characters")
        
        
        
        return is_valid