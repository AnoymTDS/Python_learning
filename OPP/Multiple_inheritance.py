

# # MULITPLE INHERITANCE

# class A:
#     def info_A(self):
#         print("we are inside class A")

# class B:
#     def info_B(self):
#         print("we are inside class B")

# class C(A,B):
#     def info_C(self):
#         print("we are inside class C")
        

# b1 = B()


# class Sand:
#     def pack_sand(self):
#         print("I am packing sand")
        
#     def wage(self):
#         return 20
        
# class Stone:
#     def carry_block(self):
#         print("I am carrying stone")
    
#     def wage(self):
#         return 20
        
# class Combined(Sand, Stone):
#     def hybrid(self):
#         print("This person can do both")
    
#     def mix_cement(self):
#         print("I can also mix cement")
        
#     def wage(self):
#         return 30

import random

class Sniper:
    
    def __init__(self,name):
        self.name = name
        self.health = 300
        self.offence = 500
        self.defence = 200
        
    def sniper_attack(self,distance,enemy):
        if distance < 30:
            self.offence /= 1.5    # 333
            value = random.randrange(int((self.offence - 50) /10), int((self.offence/10)))
            enemy.health -= value
            print(f"You have removed {value} health from {enemy.name}")
            print(f"{enemy.name} has {enemy.health} life left")
        else:
            self.offence *= 1.5    # 333
            value = random.randrange(int((self.offence - 50) /10), int((self.offence/10)))
            enemy.health -= value
            print(f"You have removed {value} health from {enemy.name}")
            print(f"{enemy.name} has {enemy.health} life left")
            
        
class Combatant:
    
    def __init__(self,name):
        self.name = name
        self.health = 300
        self.offence = 250
        self.defence = 450
        
    def combat_attack(self,distance):
        if distance < 30:
            self.offence *= 1.5    
            value = random.randrange(int((self.offence - 50) /10), int((self.offence/10)))
            return value
        else:
            self.offence /= 1.5    
            value = random.randrange(int((self.offence - 50) /10), int((self.offence/10)))
            return value


class All_rounder(Sniper,Combatant):
    
    def __init__(self,name):
        self.name = name
        self.health = 333
        self.offence = 334
        self.defence = 333
    
    def allrounder_attack(self,distance):
        if distance < 30:
            return self.combat_attack(distance)
        else:
            return self.sniper_attack(distance, enemy= 10)
            

s1 = Sniper("Alex")
c1 = Combatant("Jude")

s1.sniper_attack(16,c1)



