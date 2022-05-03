class Department(): 

    def __init__(self,name,location):
        self.name= name
        self.location = location
        self.employees= []

    def add_employee(self, )





class Employee():
    def __init__(self, first_name, last_name, salary, department, middle_name=None):
        self.first_name = first_name
        self.middle_name=middle_name
        self.last_name = last_name
        self.salary = salary 
        self.department = department
        self.department.employees.append(self)
    
    def full_name(self):
        if self.middle_name ==None:
            return f"{self.first_name}{self.last_name}"
        else:
            return f"{self.first_name}{self.middle_name}{self.last_name}"

    def change_salary(self,percent_increase):
        if percent_increase > .10:
            return None
        new_salary = self.salary * (1 + (.01 * percent_increase))
        
        if not new_salary <40000:
            self.salary = new_salary

department_a = Department("Sales", "804A")
department_b = Department("Engineering", "201B")


employee_1 = Employee("Alex", None, "Smith", 83000, department_a)
#employee_2 = Employee("Bradley", None,"Jones",85000)
#employee_3 = Employee("Charlie", "Adams",65000)
#employee_4 = Employee("Darla", "Smith", 86000, middle_name="Allison")
#employee_5 = Employee("Jeff", "Smith", 40000)
