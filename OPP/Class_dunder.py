

class Human:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.account_balance = balance

    def info(self):
        return f"This is {self.name} and this person is {self.age} years old || {self.account_balance}"

    def __str__(self):
        return f"{self.name} is {self.age} and a very rich man."

human_1 = Human("Retro", 18, 500)
#human_2 = Human("Dozie", 24)
#human_3 = Human("Ayo", 12)

#print(human_1.name)
#print(human_1.age)
#print(human_2.name)
#print(human_2.age)
#print(human_3.name)
#print(human_3.age)

def nl():
    print('\n')

nl()
#print("My name is %s and I am {} years old." %human_1.name, format(human_1.age))

#print(human_1)

print(human_1.info())
human_1.account_balance += 600