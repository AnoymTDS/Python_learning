


class Employee:
    no_of_employee = 0
    yearly_raise = 1.1

    def __init__(self,name, dept, salary):
        self.name = name
        self.dept = dept
        self.salary = salary

    @classmethod
    def from_unclean_employee_info(cls,emp_str):
        name, dept, salary = emp_str.split(",")
        return Employee(name, dept, salary)
    
    def change_salary(self):
        self.salary = self.salary * Employee.yearly_raise

    @classmethod
    def set_yearly_raise(cls,percent):
        cls.yearly_raise = percent


emp_1 = Employee("Tod","Human Resource", 2000)
emp_2 = Employee("Tine", "Logistics", 2000)

# emp_1.yearly_raise = 1.2

# Employee.set_yearly_raise(Employee,1.2)

# print(emp_1.yearly_raise)

cs1 = 'Ken Nnamani,Doctor,3500'
cs2 = 'Donald Duke,Nurse,2500'
cs3 = 'Musa Yaradua,MD,4500'

emp_cs1 = Employee.from_unclean_employee_info(cs2)

print(emp_cs1.name)


import random
def generate_id(Text):
    ids = []
    while True:
        id = random.randrange(1000,9999)
        if id not in ids:
            ids.append(id)
            return f"{Text}-{id}"
        

class Google:

    def __init__(self,name,email):
        self.id = generate_id("GOOGLE")
        self.name = name
        self.email = email
        self.youtube = Youtube(self.id, self.name, self.email)
        self.gmail = Gmail(self.id, self.name, self.email)

class Youtube(Google):

    def __init__(self,google_id,name,email):
        self.google_id = google_id
        self.id = generate_id("YOUTUBE")
        self.name = name
        self.email = email

class Gmail(Google):

    def __init__(self, google_id, name, email):
        self.google_id = google_id
        self.id = generate_id("GMAIL")
        self.name = name
        self.email = email

    
ggl_acct = Google("Daniela","Daniela@gmail.com")

print(ggl_acct.youtube.id)