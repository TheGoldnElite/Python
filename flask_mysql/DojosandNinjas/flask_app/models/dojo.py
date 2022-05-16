from config.mysqlconnection import connectToMySQL
from flask_app.models import ninja


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        dojos=[]
        results = connectToMySQL('dojosandninjas').query_db(query)
        for row in results:
            dojos.append(cls(row))
        return dojos



    @classmethod
    def create(cls,data):
        query="INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojosandninjas').query_db(query,data)

    @classmethod
    def get_dojos(cls,data):
        query= "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojos_id;"
        results=connectToMySQL('dojosandninjas').query_db(query,data)

        dojo = cls(results[0])
        for row in results:
            data= {
                "id": row['ninjas.id'],
                "first_name":row['first_name'],
                "last_name":row['last_name'],
                "created_at":row['ninjas.created_at'],
                "updated_at":row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(data))
        return dojo
