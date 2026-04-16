



# import random

# # list_one = []

# # while len(list_one) < 10:
# #     if len(list_one) < 5:
# #         list_one.append(random.randrange(1,11) * 2)
# #     else:
# #         list_one.append((random.randrange(1,11) * 2)+ 1)
            
# # print(list_one)



# # list_two = []

# # while len(list_two) < 10:
# #     if len(list_two) % 2 == 0:
# #         list_two.append(random.randrange(1,11) * 2)
# #     else:
# #         list_two.append((random.randrange(1,11) * 2) + 1)
        
# # print(list_two)


# thislist = ["apple", "banana", "cherry"]
# capital_fruits = [x.upper() for x in thislist if x.startswith("a")]

# print(capital_fruits)

# our_list =  [3,1,4,6,3,3,5,7,8,9,4,36,8,9,95,3,24,6,75,8,4,3,42]
    
# # [ for x in thislist]
    
    
    
    
# ZIP FUNCTION


# names = ["John", "Doe", "Jane", "Eve", "Adam"]

# scores = [50,60,70,80,90, 100]

# result = []

# for name, score in zip(names,scores):
#     # joined = [name,score]
#     # result.append(joined)
#     print(f"{name} - {score}")
    
# print(result)
    
    

# result = [["john",50], ["Doe", 60], [ ]]

lst1=[19542209, 4887871, 1420491, 626299, 1805832, 39865590]
lst2=["New York", "Alabama", "Hawaii", "Vermont", "West Virginia",  "California"]

lst3= []

# for ip, address in zip(lst1, lst2):
#  joined = [lst1, lst2]
#  lst3.append(joined)

#  print(f"This IP: {ip} belongs to this Address: {address}")






    
    
    
# ENUMERATE
    
# list_three = ['Apples','Banana','Coconut', 'Date', ' Figs','Grapes']


# for juju, x in enumerate(list_three):
#     print(f"Fruit({x}) at index({juju})")

# Usimg While to loop through List

# list_while = ['orange','mango','date','cherry']
# index = 0

# while index < len(list_while):
#     print(list_while[0])
#     index += 1