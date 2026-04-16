

class Grand_Father :
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def fam_background(self):
        print(self.firstname, self.lastname)

GF = Grand_Father("Mike", "Doku")
GF.fam_background()
    
def nl():
    print('\n')

nl()
class Father(Grand_Father):
    def __init__(self, first_name, last_name, sex):
        Grand_Father.__init__(self, first_name, last_name)
        self.sex = sex

    def fam_background(self):
        print(self.firstname, self.lastname, self.sex)

Fa = Father("Anthony", "Joshua", "Male")
Fa.fam_background()

nl()
class Son(Father):
    def __init__(self, fn, ln, sex, sch):
        super().__init__(fn, ln, sex)
        self.firstname = fn
        self.lastname = ln
        self.sex = sex
        self.sch = sch

    def fam_background(self):
        print(self.firstname, self.lastname, self.sex, self.sch)

So = Son("Dave", "Santan", "Male", "Middlesex")
So.fam_background()



# 1. *
# 2. **
# 3. ***
# 4. ****
# 5. *****
# 6. ******
# 5. *****
# 4. ****
# 3. ***
# 2. **
# 1. *