
quote = "All is fair in love and war"
print(quote)
print('\n')

print(quote.upper()) #uppercase
print('\n')
print(quote.lower()) #lowercase
print('\n')
print(quote.title()) #tile case
print('\n')
print(len(quote)) #count characters
print('\n')

name = "Toby" #string
age = 17 #int
gpa = 3.7 #float - has a decimal

print(int(age))
print(int(30.1)) #It gives the whole number without rounding the decimal up
print("My name is " + name + " and I am " + str(age) + " year old.")
age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n')
#FUNCTIONS

def who_am_i(): #this is a function without parameters
    name = "Tobi" #local variable
    age = 16
    print("My name is " + name + " and I am " + str(age) + " year old.")

who_am_i()
print(age)

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(20)

def add(x,y):
    print(x + y)

add(7,7)

def multiply(x,y):
    return x * y 

multiply(7,7)
print(multiply(7,7))

def square_root(x):
    print(x ** .5)

square_root(25)

def nl():
    print('\n')

nl()

#BOOLEAN EXPRESSIONS (TRUE OR FALSE)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()
#RELATION AND BOOLEAN OPERATIONS
greater_than = 7 > 5
less_than = 5 < 7
greate_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 < 5) or (5 < 7) #True

test_not = not True #False

nl()
#CONDITIONAL STATEMENT - if/else

def drink(money):
    if money >= 2:
            return "You've got yourself a drink!"
    else:
            return "No drink for you!"
    
print(drink(3))
print(drink(1))

nl()
def alcohol(age, money):
     if (age >= 18) and (money >= 5):
          return "We're getting a drink!"
     elif (age >= 18) and (money < 5):
          return "Come back with more money."
     elif (age < 18) and (money >= 5):
          return "Nice try, kid!"
     else:
          return "You're too young and don't have enough money!"
     
print(alcohol(18, 5))
print(alcohol(18, 4))
print(alcohol(17, 5))
print(alcohol(17, 4))

nl()
#LISTS - Have brackets []
movies = ["When Harry Met Sally", "Top Boy", "The Exorcist", "Harry Potter", "Spiderman"]

print(movies[0]) #returns the first item in the list, which is the first index number given
print(movies[1])
nl()
print(movies[0:3] ) #return the first index number given right until the last number, but not include the last number, but not include the last number
nl()
print(movies[0:]) #return first index number given to the last because of the absensce of a number to stop
nl()
print(movies[:1])
nl()
print(movies[:4])
nl()
print(movies[:])
nl()
print(movies[-1])
nl()
print(len(movies))
print(movies)
nl()
movies.insert(2, "Hustle")
print(movies)
nl()
movies.pop(2)
print(movies)

tolani_movies =["Wura", "The Real House Wives Of Lagos", "Summer I Turned Pretty"]
our_favorite_movies = movies + tolani_movies
print(our_favorite_movies)
nl()
grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1] = 83
print(bobs_grade)
grades[0][1] = 83
print(grades)

nl()
#Tuples - Do not change, ()
grades = ("a", "b", "c", "d", "f")

print(grades[1])

nl()
#LOOPING

#For loops - start to finish of an iterate
vegatables = ["cucumber", "spinach", "cabbage"]
for x in vegatables:
     print(x)

#While loops - execute as long as True
i = 1

while i <= 10:
     print(i)
     i += 1

nl()
#ADVANCED STRINGS

my_name = "Tobi"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence"

print(sentence[:4])
print(sentence.split()) #delimeter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
print(quote)
quote = "He said, \"give me all your money.\""
print(quote)

too_much_space = "            hello       "
print(too_much_space.strip())

#Case Type Testing 
print("A" in "Apple") #True
print("a" in "Apple") #False

letter = "A"
word = "Apple"
print(letter.lower() in word.lower())

movie = "Top Boy"
#Print Format
print("My Favorite movie is {}.".format(movie))
print("My favorite movie is %s." %movie)
print(f"My favorite movie is {movie}.")


nl()
#Dictionaries - key/value pairs {}

drinks = {"Pepsi": 100, "Fanta": 200, "coke": 250} #drink is the key, price is the value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)

employees['Legal'] = ["Mr. Frond"] #adds new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)

drinks["Pepsi"] = 250
print(drinks)

print(drinks.get("Pepsi"))