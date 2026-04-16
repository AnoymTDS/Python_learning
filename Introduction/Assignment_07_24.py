

import random
import string


# def password_generator(length, count):
#     passwords = []
#     for x in range(count):
#         password = ''.join(random.choice(string.ascii_letters+string.digits+string.punctuation)for y in range(length))
#         passwords.append(password)
#     return passwords

# print(password_generator(7,10))

# def detector(*args):
#     if type(args)==list:
#         return sum(args)
    
#     elif type(args[0]) in (int, float):
#         return sum(args)
#     else:
#         return "Invalid Input! Please try again"
    

# print(detector(57,78,98))

def mul_tsk_detector(*args):
    sum_val = 0
    for x in args:
        if type(x)==list:
            sum_val += sum(x)
        elif type(x) in (int, float):
            sum_val += x
        else:
            print("Invalid input, Try again!")
    return sum_val
            


print(mul_tsk_detector([3,577,43,35],1,2))


# def bonus_dect(*args):
#     t_sum = 0
#     for x in args:
#         while type(x) == list:
#             t_sum += sum(x)
#             break
#         while True:
#             if type(x) in (int,float):
#              t_sum += sum(x)
#             break
#     return t_sum


# print(bonus_dect(4,5,5))        
    

    