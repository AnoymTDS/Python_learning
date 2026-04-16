

def nl():
    print('\n')

txt = "hello, world"

print(txt[-10:-7])

nl()
texts = "APTECH"

c = texts[ : : 3]
print(c)

#Modification of  Strings
nl()
text = "Hello, world!"
print(text.title())
print(text.upper())
print(text.capitalize())
print(text.lower())

nl()
a = "Hello, World!"
print(a.replace("H", "J"))
print(a.replace("o", "e",1))

nl()
#Formattin String

age = 36
money = 100

txts = f"hello my name is david, and i am {age} years and i have {money} in my bank"
print(txts)