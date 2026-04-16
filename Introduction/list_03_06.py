


# import random


# list_one = []

# while len(list_one) < 10:
#     if len(list_one) < 5:
#         list_one.append(random.randrange(1,11) * 2)
#     else:
#         list_one.append((random.randrange(1,11) * 2) + 1)
# print(list_one)

# list_two = []

# while len(list_two) < 10:
#   if len(list_two) % 2 == 0:
#         list_two.append(random.randrange(1,11) * 2)
#   else:
#       list_two.append((random.randrange(1,11) * 2) + 1)
# print(list_two)

# list_three = []

# while len(list_three) < 10:
#     if len(list_three) % 3 != 2:
#         list_three.append(random.randrange(1,11) * 2)
#     else:
#         list_three.append((random.randrange(1,11) * 2) + 1)
# print(list_three)

# thisislist = ["apple", "banana","cherry"]

# for _ in thisislist:
#     print(_.upper())

# our_list = [3,1,46,3,3,5,7,8,9,4,32,8,9,95,3,24,6,73,8,4,3,42]

# my_lists = [x * 10 for x in our_list if x % 2 == 0]

# print(my_lists)

#ZIP FUNCTION

# names = ["John","Doe","Jane","Eve","Adam"]

# scores = [50,60,70,80,90]

# for name, score in zip(names,scores):
#     x =[name,score]

# result = [["John",50], ["Doe",60], []]

# #Enumerate

# list_three = ['Apples','Banana','Coconut','Date','Figs','Grapes']

# for idx, x in enumerate(list_three):
#     print(f"Fruits ({x}) at index ({idx})")

thisislist = ["apple","bread","fish"]
print(len(thisislist))