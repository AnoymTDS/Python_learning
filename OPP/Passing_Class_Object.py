
import random

def accout_num_gene():
    x = random.randrange(100000,10000000)
    return x
    
    
    
class Student:
    
    def __init__(self,student_id,student_name,student_age):
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        
    def __str__(self):
        return self.student_name
    
        
class Course:
    
    def __init__(self,course_name,course_units,max_students):
        self.course_name = course_name
        self.course_units = course_units
        self.max_students = max_students
        self.student_list = []
        self.course_id = accout_num_gene()
        
    def register_student(self,student): # passing a student obj
        if len(self.student_list) < self.max_students:
            self.student_list.append(student)
            print(f"{student.student_name} have been registered succesfully!")
        else:
            print(f"{student.student_name} Class is full")
    
    # def __str__(self):
    #     return self.course_name
    
    
student_1 = Student("001", "Adam", 30)
student_2 = Student("002", "Bentley", 20)
student_3 = Student("003", "Audi", 25)

course_1 = Course("Python", 6, 2)

course_1.register_student(student_1)
course_1.register_student(student_2)
course_1.register_student(student_3)


# print(course_1)

for x in course_1.student_list:
    print(x)