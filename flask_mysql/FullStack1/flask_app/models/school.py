from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import witcher


class School:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=['created_at']
        self.updated_at=['updated_at']

    witchers=[]





    this_school = cls(results[0])

    for row_from_db in results:
        witcher data={
            "id":row_from_db["witchers.id"],
            "name":row_from_db["witchers.name"],
            "age":row_from_db["witchers.age"],
            "created_at":row_from_db["witchers.created_at"],
            "updated_at":row_from_db["witchers.updated_at"],
            "school_id": row_from_db["school_id"]
            
        }
        this_school.witchers.append(witcher.Witcher(witcher_data))

    return this_school