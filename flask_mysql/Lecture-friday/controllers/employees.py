@app.route('employees/new',methods=['POST'])
def new_employees():

    if request.form['department_id'] =='-1':
        return redirect('/')

    new_employee_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'salary': request.form['salary'],
        'department_id': request.form['department_id'],
    }

    if Employee.validate_employee(new_employee_data):   



