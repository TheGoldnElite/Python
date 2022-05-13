














    @classmethod
    def get_employee_by_id(cls,data):
        query= 'SELECT * FROM employees WHERE id= %(employee_id)s;'

        results = connectToMySQL('apr_employees').query_db(query,data)









