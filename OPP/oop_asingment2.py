class Staff:
    def __init__(self, salary, levels):
        self.salary = salary
        self.__levels = levels
    
    def salary_paid(self):
        pass
    
    def get_levels(self):
        return self.__levels
    
    def change_level(self, promotion):
        self.__levels = promotion

class Security(Staff):
    def __init__(self, department, salary, levels):
        self.department = department
        super().__init__(salary, levels)
        
    def salary_paid(self):
        print(f"Salary paid: {self.salary}")
        
class Cashier(Staff):
    def __init__(self, department, salary, levels):
        self.department = department
        super().__init__(salary, levels)
        
    def salary_paid(self):
        print(f"Salary paid: {self.salary}")

class Customer_Service_Representative(Staff):
    def __init__(self, department, salary, levels):
        self.department = department
        super().__init__(salary, levels)
        
    def salary_paid(self):
        print(f"Salary paid: {self.salary}")

class Department_Manager(Staff):
    def __init__(self, department, salary, levels):
        self.department = department
        super().__init__(salary, levels) 
        
    def salary_paid(self):
        print(f"Salary paid: {self.salary}")

class SeniorAccountant(Staff):
    def __init__(self, department, salary, levels):
        self.department = department
        super().__init__(salary, levels)
    
    def pay_salary(self, staff):
        if staff.get_levels() > 5:
            print(f"{staff.department} salary has been paid")
        else:
            print("The junior accountant will pay it")
            
class JuniorAccountant(Staff):
    def __init__(self, department, salary, levels):
        self.department = department
        super().__init__(salary, levels)
    
    def pay_salary(self, staff):
        if staff.get_levels() < 5:
            print(f"{staff.department} salary has been paid")
        else:
            print("You can't pay their salary")
            
            
            
security= Security("security",20000,2)
cashier= Cashier("cashier",25000,4)
customer_service_representative=Customer_Service_Representative("customer_service_representative",80000,6)
department_manager = Department_Manager("department_Manager",100000,8)
SA = SeniorAccountant("senior_Accountant",80000,6)
JA = JuniorAccountant("junior_Accountant",50000,5)
SA.pay_salary(department_manager)