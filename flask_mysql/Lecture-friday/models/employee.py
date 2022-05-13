
@classmethod
    def update_employee(cls,data):
        query = "UPDATE employees SET frist_name = %(first_name)s,middle_name"

        result =connectToMySQL("apr_employees").query_db(query,data)

        return result

    @staticmethod
    def validate_employee(data):

        is_valid=True

        first_name_regex= re.compile(r"[A-Z]{1}[a-zA-Z.\-'!]{0-49}")

        if not first_name_regex.match(data['first_name']):
            flash("jfdaskljflskda")
            is_valid = False







        if data['first_name']
            is_valid=False
        elif len(data['first_name']) > 50:
            is_valid=False

        if data['middle_name'] != None:
            if len(data['middle_name']) > 50:
                is_valid=False
        
        if data['last_name'] =='':
            is_valid=False
        elif len(data['last_name']) > 50:
            is_valid=False


        try:
            salary=int(data['salary'])
        except:
            is_valid=False

        if data['department_id'] == '-1':
            is_valid =False

        return is_valid

        
        
        
        
        
        
        
        
        
        
        
        
        
     

