#File Handling

# "r" -> read a file
# "w" -> write to a file
# "a" -> append to the file
# "x" -> create a file

# creating a file
# file = open("filetwo.txt","x")

#write to a file(if the file is not existing write will create it)
# file = open("filetwo.txt","w")
# appending more than one to a file
# file = open("Modules_work\\files\\fileone.txt","a")
# file.write("daniella is the G.O.A.T  --- facts\n")

# using write lines
# data = ["Good 1 - Good 2\nBetter 1 - better 2"]
# file.writelines(data)

#reading from a file
# file = open("Modules_work\\files\\filetwo.txt","r")
# print(file.readlines())
# print(file.read())

# deleting from a file
import os
# file = open("Modules_work\\files\\filetwo.txt","r")
# file.close()
# os.remove("Modules_work\\files\\filetwo.txt")

# classwork

file = open("Modules_work\\files\\filetwo.txt","r")
file_one = open("Modules_work\\files\\fileone.txt","w")

text = file.read()

vowels ="aeiou"
new_text = ""


for char in text:
    if char not in vowels:
        new_text +=char.upper()

print(new_text)

file_one.write(new_text)

file.close()


