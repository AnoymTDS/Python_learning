#LAMBDA


# add_ten = lambda x : x + 10
# print(add_ten(10))


# cal_mul = lambda x,y,z: (x+y)-z
# print(cal_mul(20,10,5))

# my_list = [1,2,3,4,5,6,7,8,9,10]

# even = filter(lambda x : x % 2 == 0 ,my_list)
# print(list(even))

#RECURSION
# def factorial(x):
#   if x == 1:
#     return 1
#   else:
#     return x * factorial(x-1)

# print(factorial(5))


#args and kwargs


import random
from sys import api_version
from urllib import request


# def whatever(*agrs):
#   for x in agrs:
#     print(x)

# whatever("hello",4,9,0,23)



# numbers = [random.randrange(1,10) for y in range(20)]
# def my_sum(*agrs):
  
#   sum = 0
#   for x in agrs[0]:
#     sum+= x
#   print(sum)

# my_sum(numbers)


#KWARGS

# def my_func(*args, **kwargs):
#   print(args)

#   print(kwargs)


# my_func("ben","ken","ten",[1,2,3],colour = "blue",age = 2)




#Test Assignment





header = input("")
content = input("")




# request
# working with api
# multithreading