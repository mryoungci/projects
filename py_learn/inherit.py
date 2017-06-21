class ShoolMember:

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("Initializing ShoolMember:",self.name)

    def tell(self):
        print("Name:%s,Age:%s,Sex:%s" %(self.name,self.age,self.sex))

class Teacher(ShoolMember):

    def __init__(self,name,age,sex,salary):
        ShoolMember.__init__(self,name,age,sex)
        self.salary = salary
        print("Initializing Teacher:",self.name)

    def tell(self):
        ShoolMember.tell(self)
        print("Salary:%d" %(self.salary))

class Student(ShoolMember):

    def __init__(self,name,age,sex,mark):
        ShoolMember.__init__(self,name,age,sex)
        self.mark = mark
        print("Initializing Student:",self.name)

    def tell(self):
        ShoolMember.tell(self)
        print("Makr:%d" %(self.mark))

t = Teacher("chen",45,"M",30000)
s = Student("yang",23,"M",96)
print()
members = [t,s]
for member in members:
    member.tell()

