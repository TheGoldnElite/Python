from symtable import SymbolTableFactory


employees = []

employees.append({"first_name":"Alex","last_name":"Smith","salary":87000})
employees.append({"first_name":"Alex","last_name":"Smith","salary":87000})
employees.append({"first_name":"Alex","last_name":"Smith","salary":87000})

#new employee
employees.append({"first_name": "Jeff","last_name":"Herbstritt","salary":28383})

#another new employee
employees.append({"first_name": "eeee","last_name":"Smith","salary":98000})


for employee in employees:
    print(f"First name: {employee['first_name']},last name:{employee['last_name']},salary:{employee['salary']}")

print("increasing salary...")
for employee in employees:
    employee["salary"] = employee["salary"] * 1.05

print("After increase")
for employee in employees:
    print(f"First name:{employee['first_name']},last_name:{employee['last_name']},salary:{employee['salary']}")




class Employee():
    def __init__(self, first_name, last_name, salary, middle_name=None):
        self.first_name = first_name
        self.middle_name=middle_name
        self.last_name = last_name
        self.salary = salary 
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
        
employee_1 = Employee("Alex", None, "Smith",83000)
employee_2 = Employee("Bradley", None,"Jones",85000)
employee_3 = Employee("Charlie", "Adams",65000)
employee_4 = Employee("Darla", "Smith", 86000, middle_name="Allison")
employee_5 = Employee("Jeff", "Smith", 40000)

employees = [employee_1, employee_2,employee_3,employee_4]

for employee in employees:
    print(f"Full name:{employee.full_name()},salary: {employee.salary}")
    
        
for employee in employees:
    employee.change_salary(-3)