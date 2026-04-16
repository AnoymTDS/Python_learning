# Abstraction


"""from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    
    def speak(self):
        print("Bark")


a1 = Dog("Bingo", 3)"""


#STATIC METHODS

"""import random
import math



class Aptech:

    @staticmethod
    def add_two(x,y):
     return x+y

    @staticmethod
    def generate_pin(num):
        pin = ""
        for x in range(num):
            number = random.randrange(10)
            pin += str(number)
        return pin

print(Aptech.add_two(40,60))
"""


#STATIC ATTRIBUTES

class Census:
    # static attribute
    national_population = 0
    non_national_population = 0

    def __init__(self, state, population):
        self.state = state
        self.population = population

    def count(self, person):
        self.population += 1
        if person.nationality == "Nigerian":
            Census.national_population += 1
        else:
            Census.non_national_population += 1

class Person:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return self.name

lagos_people = []
abuja_people = []
for x in range(100):
    if x % 33 == 0:
        person = Person(f"lagos_person{x}", "Nigerian")
    else:
        person = Person(f"lagos_person{x}", "Lebanese")
    lagos_people.append(person)

    for x in range(100):
     if x % 33 == 0:
        person = Person(f"abuja_person{x}", "Nigerian")
    else:
        person = Person(f"abuja_person{x}", "Lebanese")
    abuja_people.append(person)

Lagos_Census = Census("Lagos", 0)

Abuja_Census = Census("Abuja", 0)

for p in lagos_people:
    Lagos_Census.count(p)

for p in abuja_people:
    Abuja_Census.count(p)

print("Census Over")


print(Lagos_Census.population)
print(Abuja_Census.population)

print(Lagos_Census.national_population)
print(Lagos_Census.non_national_population)
    
# Census.count(lagos_people[0])
# print("Nationals: ", Census.national_population)
# print("Non-nationals: ", Census.non_national_population)