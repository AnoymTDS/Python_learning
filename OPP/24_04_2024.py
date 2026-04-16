


# class Person:
#     def __init__(self,name,age):
#         self.__name = name
#         self. age = age

#     @property
#     def Name(self):
#         return self.__name
    
#     @Name.setter
#     def Name(self, new_name):
#         self.__name = new_name


# p1 = Person("Daniela", 65)
# p1.age = 30

# # print(p1.age)

# print(p1.Name)
# p1.Name = "Daniel"
# print(p1.Name)



# class BankCustomer:
#     def __init__(self,name,problem,money):
#         self.name = name
#         self.money = money
#         self.__problem = problem

#     def news(self):
#         print(f"{self.name} your are too broke to solve your problem")

#     @property
#     def problem(self):
#         return self.__problem
    
#     @problem.setter
#     def problem(self, value):
#         if self.money > (self.__problem ** 4):
#           self.__problem = value
#         else:
#             self.news()
            


# c1 = BankCustomer("chike",70,3000000000000)

# c1.problem = 203




class DarkStores:
    def __init__(self,salary,level):
        pass


class Manager(DarkStores):
    pass


class Cleaner(DarkStores):
    pass