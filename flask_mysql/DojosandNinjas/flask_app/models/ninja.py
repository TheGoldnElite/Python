from config.mysqlconnection import connectToMySQL
from flask_app.models import dojo


class Ninja:
    def __init__(self,data):
        self.id =data['id']
        self.first_name =data['first_name']
        self.last_name =data['last_name']
        self.age =data['age']
        self.created_at =data['created_at']
        self.updated_at =data['updated_at']
        self.dojo_id = data['dojo_id']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        ninjas=[]
        results =  connectToMySQL('dojosandninjas').query_db(query)
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (dojos_id,first_name,last_name,age) VALUES (%(dojos)s, %(first_name)s,%(last_name)s,%(age)s"
        return connectToMySQL('dojosandninjas').query_db(query,data)

