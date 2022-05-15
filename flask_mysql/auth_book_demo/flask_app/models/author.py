from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book


#add author part
class Author:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        

    
    #from sql table
    #(%()s == data from key in author_controller.py
    @classmethod
    def create_author(cls,data)
        query="INSERT INTO authors (first_name,last_name,created_at,updated_at) VALUES (%(first_name)s, %(last_name)s,NOW(),NOW());"
        results= connectToMySQL('auth_book_schema').query_db(query,data)
        return results

    @classmethod
    def get_all_authors(cls):
        query="SELECT * FROM authors;"
        results= connectToMySQL('auth_book_schema').query_db(query)
        authors=[]
        for one_auth in results:
            authors.append(cls(one_auth))
            return authors


    @classmethod
    def get_one_author(cls,data):
        query = "SELECT * FROM authors LEFT JOIN books ON author_id = authors.id WHERE authors.id = %(author_id)s;"
        results= connectToMySQL('auth_book_schema').query_db(query,data)

        author=cls(results[0])

        for row in results:
            
            book_data = {
                "id":row['books.id'],
                "row":['title'],
                "language":row['language'],
                "pages":row['pages'],
                "author_id":row['author_id'],
                "description_id":row['description_id'],
                "created_at":row['created_at'],
                "updated_at":row['updated_at'],
                #"author": {}
            }

            author.books.append(book.Book(book_data))
        return author


