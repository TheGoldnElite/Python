from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user


class Activity():
    def __init__(self,data):
        self.id=data['id']
        self.event_name=data['event_name']
        self.location=data['location']
        self.description=data['description']
        self.date=data['date']
        self.members=data['members']
        # self.time=data['time']
        self.updated_at=data['updated_at']
        self.created_at=data['created_at']
        self.user_id=data['user_id']
        self.owner = {}
        

    @staticmethod
    def validateactivities(data):
        is_valid=True
        if (len(data['event_name'])) < 3:
            flash("The Event Name must be more than three characters long")
            is_valid=False
        if (len(data['location'])) < 3:
            flash("Location must be more than three characters long")
            is_valid=False
        if (len(data['description'])) < 3:
            flash("Description must be more than three characters long")
            is_valid=False
        if (len(data['date'])) < 3:
            flash("Date must be put in")
            is_valid=False
        # if (len(data['time'])) < 1:
        #     flash("Time must be put in")
        #     is_valid=False
        if ((data['members'])) == '':
            flash("Member amount must be put in")
            is_valid=False
        elif int(data['members']) < 1:
            flash("Members must be more than 1")
            is_valid=False

        return is_valid

    

    @classmethod
    def save_activities(cls,data):
        query="INSERT INTO activities(event_name,location,description, date, members,updated_at,created_at,user_id) VALUES (%(event_name)s,%(location)s,%(description)s,%(date)s,%(members)s,NOW(),NOW(),%(user_id)s);"
        results=connectToMySQL("pickup_schema").query_db(query,data)
        return results
    
    
    @classmethod
    def get_all_activities(cls):
        print("get_all_activities")
        query = "SELECT * FROM activities LEFT JOIN users ON users.id = activities.user_id;"
        results=connectToMySQL("pickup_schema").query_db(query)

        all_activities = []
        
        for row in results:
            activity=cls(row)
            user_data = {
                "id":row['users.id'],
                "first_name":row['first_name'],
                "last_name":row['last_name'],
                "email":row['email'],
                "password":row['password'],
                "created_at":row['users.created_at'],
                "updated_at":row['users.updated_at'],
            }

            activity.owner=user.User(user_data)
            all_activities.append(activity)
        return all_activities

    @classmethod
    def activity_get_one(cls,data):
        query="SELECT * FROM activities LEFT JOIN users ON users.id = activities.user_id WHERE activities.id =%(activity_id)s;"
        results=connectToMySQL("pickup_schema").query_db(query,data)
        
        activity =cls(results[0])

        user_data = {
            "id":results[0]['users.id'],
            "first_name":results[0]['first_name'],
            "last_name":results[0]['last_name'],
            "email":results[0]['email'],
            "password":results[0]['password'],
            "created_at":results[0]['users.created_at'],
            "updated_at":results[0]['users.updated_at']
        }
        activity.owner = user.User(user_data)
        return activity

    @classmethod
    def updatepage(cls,data):
        query="UPDATE activities SET event_name=%(event_name)s,location=%(location)s,description=%(description)s,date=%(date)s,members=%(members)s,updated_at=NOW(),created_at=NOW() WHERE id= %(activity_id)s;"
        results=connectToMySQL("pickup_schema").query_db(query,data)
        return 

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM activities WHERE id=%(activities_id)s;"
        results=connectToMySQL("pickup_schema").query_db(query,data)
        return
        

    @classmethod
    def one_activity(cls,data):
        query="SELECT * FROM activities LEFT JOIN users ON users.id = activities.user_id WHERE activities.id =%(activity_id)s;"
        results=connectToMySQL("pickup_schema").query_db(query,data)
        
        activity =cls(results[0])

        user_data = {
            "id":results[0]['users.id'],
            "first_name":results[0]['first_name'],
            "last_name":results[0]['last_name'],
            "email":results[0]['email'],
            "password":results[0]['password'],
            "created_at":results[0]['users.created_at'],
            "updated_at":results[0]['users.updated_at']
        }
        activity.owner = user.User(user_data)
        return activity