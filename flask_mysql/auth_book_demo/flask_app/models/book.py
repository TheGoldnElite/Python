from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import author


#from book table sql
class Book:
    def __init__(self,data):
        self.id=data['id']
        self.title=data['title']
        self.language=data['language']
        self.pages=data['pages']
        self.author_id=data['author_id']
        self.description_id=data['description_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

        self.author= {};

    @classmethod
    def create_book(cls,data):
        query ="INSERT INTO books(title,pages,language,description,author_id,created_at,updated_at) VALUES(%(title)s,%(pages)s,%(language)s,%(description)s,%(author_id)s,NOW(),NOW());"

        results= connectToMySQL('auth_book_schema').query_db(query,data)
        return results


    @classmethod
    def get_books_with_authors(cls):
        query = "SELECT * FROM books LEFT JOIN authors ON author_id = authors.id;"
        results = connectToMySQL('auth_book_schema').query_db(query)
        books=[]
        
        for row in results:
            book=cls(row)
            author_data = {
                "id":row['authors.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.author = author.Author(author_data)
            books.append(book)
        return books

    
    @classmethod
    def get_one_book(cls,data):
        query = "SELECT * FROM books LEFT JOIN authors ON author_id = authors.id WHERE books.id =%(book_id)s;"
        results = connectToMySQL('auth_book_schema').query_db(query,data)
        book = cls(results[0])
        author_data = {
                "id":results[0]['authors.id'],
                "first_name": results[0]['first_name'],
                "last_name": results[0]['last_name'],
                "created_at": results[0]['authors.created_at'],
                "updated_at": results[0]['authors.updated_at']
            }
            book.author=author.Author(author_data)
            return book

    @classmethod
    def update_book_info(cls,data):
        query = "UPDATE books SET title = %(title)s,language=%(language)s,description = %(description)s,pages=%(pages)s,author_id=%(author_id)s, updated_at=NOW() WHERE id=%(book_id)s"
        results = connectToMySQL('auth_book_schema').query_db(query,data)
        return

    @classmethod
    def delete_one_book(cls,data):
        query = "DELETE FROM books WHERE id=%(book_id)s;"
            results = connectToMySQL('auth_book_schema').query_db(query,data)
            return




