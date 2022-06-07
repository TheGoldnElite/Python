from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user



class Project():
    def __init__(self,data):
        self.id=data['id']
        self.description=data['description']
        self.name=data['name']
        self.dimensions=data['dimensions']
        self.instructions=data['instructions']
        self.updated_at=data['updated_at']
        self.created_at=data['created_at']
        self.user_id=data['user_id']
        self.owner={}

    
    
    @staticmethod
    def validateproject(data):
        is_valid=True
        if (len(data['name'])) < 3:
            flash("Description must be more than three characters long")
            is_valid=False
        if (len(data['description'])) < 3:
            flash("Description must be more than three characters long")
            is_valid=False
        if (len(data['dimensions'])) < 3:
            flash("Dimensions must be more than three characters long")
            is_valid=False
        if (len(data['instructions'])) < 3:
            flash("Instructions must be more than three characters long")
            is_valid=False

        return is_valid

