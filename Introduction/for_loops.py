

#text = "international"

#for letter in text:
#    print(letter)

#for num in range(4):
#    print(num)

# my_num = [2,4,5,7,0,4]

# for x in my_num:
#     print(x, my_num) 

# for x in range(1,11):
#     if x % 2 == 0:
#         print(x)

# num = 3
# for x in num:
#       pass

# x = 0
# while x < 5:
#     print(f"Hello this is the number {x}")
#     if x == 3:
#         break
#     x += 1

# for x in range(10):
#         if x == 7:
#             continue
#         print(x)
#         print("deja vu")

user_input = int(input("pick a number: "))
#print(user_input)
#print(type(user_input))
for num in range(1, 13):
  print(f"{user_input} x {num} = {num * user_input}")