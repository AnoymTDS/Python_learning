


from email.errors import MalformedHeaderDefect


class Libary:
    def __init__(self,title,author,year_of_release):
        self.title = title
        self.author = author
        self.year_of_release = year_of_release

    def info(self):
        pass

class Book(Libary):
     def info(self):
        print(f"{self.title}")


class Dvd(Libary):
     def info(self):
        print(f"{self.title}")


class Cd(Libary):
     def info(self):
        print(f"{self.title}")




class Payroll_for_Employees:
    def __init__(self,hourly_wages,salary, contract_duration):
       self.hourly = hourly_wages
       self.salary = salary
       self.con_dura = contract_duration

    def weekly_pay(self):    
        pass


class Full_time(Payroll_for_Employees):
    def info(self):
        print(f"{self.salary}")
    
    def weekly_pay(self):
        print(f"you're not eligeble for weekly pay")


class Part_time(Payroll_for_Employees):
    def info(self):
        print(f"{self.hourly}")
    
    def weekly_pay(self):
        print(f"You're eligeble for weekly pay")


class contractors(Payroll_for_Employees):
    def info(self):
        print(f"{self.con_dura}")
    
    def weekly_pay(self):
        print(f"You're not eligeble for weekly pay")



class VehiclesItems:
    def __init__(self,make,model,year_of_manufacture):
        self.make = make
        self.model = model
        self.yof = year_of_manufacture

    def fuel_eff(self):
        pass


class Car(VehiclesItems):
    def __init__(self, make, model, year_of_manufacture):
        super().__init__(make, model, year_of_manufacture)
    
    def fuel_eff(self):
        pass


class Truck(VehiclesItems):
    def __init__(self, make, model, year_of_manufacture):
        super().__init__(make, model, year_of_manufacture)
    
    def fuel_eff(self):
        pass


class Motorcycles(VehiclesItems):
    def __init__(self, make, model, year_of_manufacture):
        super().__init__(make, model, year_of_manufacture)
    
    def fuel_eff(self):
        pass


