


# class Human:
#    def __init__(self,name,age,sex): 
#       self.name = name
#       self.age = age
#       self.sex = sex

#    def birthday(self):
#     print("Happy Birthday!!!")
#     self.age += 1

#    def __str__(self):
#       return f"{self.name} | {self.age}"
   

# p1 = Human("Josh",17,"Male")
# p2 = Human("Shade",17,"Female")

# print(p2.age)
# p2.birthday()
# print(p2.age)


class Car:
  def __init__(self, name, colour, min_speed, max_speed,value):
      self.name = name
      self.colour = colour
      self.min_speed = min_speed
      self.max_speed = max_speed
      self.value = value
   
  def depreciation(self):
      print("Car value has depreciated")
      self.value = self.value*0.2
      return self.value

c1 = Car("Audi","Space black",167,378,700000)
c2 = Car("Lamboghini","Orange",280,398,483999)


# print(c1.name)
print(c2.name)
print(c2.value)
c2.depreciation()
print(c2.value)