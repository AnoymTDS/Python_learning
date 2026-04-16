

# Single Inheritance


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def get_name(self):
#         print(f"Animal name is {self.name}")


# class Dog(Animal):
#     def __init__(self, name, food_cat):
#         super().__init__(name)
#         self.food_cat = food_cat

# dog1 = Dog("Bingo","omnivore")
# ani = Animal("Owl")

#Multi Level Inheritance


# class Parent:
#     def __init__(self, family_name):
#         self.f_name = family_name


# class Child(Parent):
#     pass


# class GrandChild(Child):
#     pass

#Multi Inheritance


# class A:
#     def info_A(self):
#       print("Informaion of A")


# class B:
#     def info_B(self):
#       print("Informaion of B")


# class C(A,B):
#     pass

# c1 = C()


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("Animal makes sounds")
        

# class Dog(Animal):
#     def speak(self):
#         print("Dogs Bark")


# class Cat(Animal):
#     def speak(self):
#         print("Cats Meow")

# dog1 = Dog("Jack")


# class Python:
#     def __init__(self, teacher, no_stud):
#         self.teacher = teacher
#         self.no_s = no_stud

#     def register(self, obj):
#         print(f"{obj.name} you have been registered.")


# class Students:
#     def __init__(self, name):
#         self.name = name

# aptech_python = Python("Mr Victory", 20)
# student_1 = Students("Tobi")

# aptech_python.register(student_1)

#create a class subject which would have a name and maximum student for it


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
        # self.course_id = accout_num_gene()
        
    def register_student(self,student): # passing a student obj
        if len(self.student_list) < self.max_students:
            self.student_list.append(student)
            print(f"{student.student_name} have been registered for {self.course_name} succesfully!")
        else:
            print(f"{student.student_name} Class is full")

    def write_exams(self):
        pass


s1 = Student("001","Tobi",17)
s2 = Student("002","Doings",18)
s3 = Student("003","Retro",18)
s4 = Student("004","Dom",16)
s5 = Student("005","Papi",20)

c1 = Course("Python",6,3)
c2 = Course("Java",4,5)

c1.register_student(s1)
c1.register_student(s2)
c1.register_student(s3)
c1.register_student(s4)
c2.register_student(s5)