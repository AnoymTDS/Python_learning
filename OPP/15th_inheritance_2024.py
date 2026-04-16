


class Person:
    def __init__(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name
        # self.networth = 100

        print("Hello this is the init of the Person")
   
    def print_full_name(self):
        print(f"My name is {self.f_name} {self.l_name}")

    def print_fname(self):
       print(f"My first name is {self.f_name}")

    def print_lname(self):
       print(f"My last name is {self.l_name}")

# p1 = Person("James","Adoo")
# p1.print_full_name()


#inherit

class Child(Person):
    def __init__(self, f_name, l_name,graduation):
        super().__init__(f_name,l_name)
        self.graud = graduation
        
        print("Hello this is the init of the child")

    def cal_grad_years(self):
        return f"You graduated {2024 - self.graud} years ago"
    


c1 = Child("Frank", "Edoho", 2020)
# c1.print_full_name()
print(c1.cal_grad_years())



class BankAccount():
    def __init__(self,acc_balance, acc_number):
        self.account_balance = acc_balance
        self.account_number = acc_number

    def deposit_funds(self, amt):
        self.account_balance = self.account_balance + amt
        
        
        print(f"You've deposited {amt} into your account.")

    def withdraw_funds(self,amt):
        self.account_balance = self.account_balance - amt

        print(f"{amt} has been Withdrawn from account now you have {self.account_balance} left")

class Savings(BankAccount):
    def __init__(self, acc_balance, acc_number):
        super().__init__(acc_balance,acc_number)

    def deposit_funds(self, amt, interest_rate = 1):
        self.account_balance = self.account_balance + amt + (amt * interest_rate)

class Current(BankAccount):
        def __init__(self, acc_balance, acc_number):
            super().__init__(acc_balance, acc_number)

        def withdraw_funds(self, amt, service_fee):
           self.account_balance = self.account_balance - amt - service_fee


#create a class called bank acc it shold have intanc acc bal, and acc num have two method deposit and withdraw 
#sub class called savings acc it shoul inherit from bank acc then add instance var call interest rate interest rate 
#should affect the deposite meth if the bank is savings create sub class current acc have an attribute called service 
#fee it affects withdrawal