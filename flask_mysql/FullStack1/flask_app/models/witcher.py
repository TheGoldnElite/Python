from flask_app.config.mysqlconnection import connectToMySQL

class Witcher:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.age=data['age']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.school_id=data['school_id']


@classmethod
def get_all_witcher (cls,data):
    query="SELECT * FROM witchers;"

    results=connectToMySQL('').query_db(query)

@classmethod
def create_witcher(cls,data):



