'''
class Student:
    "this is student class"


# print(Student.__doc__)
print(Student)
help(Student)

'''


# 1. Instance Methods 

'''
class Student:
    """This is the Student class with required data"""
    
    def __init__(self):
        self.roll=100
        self.name="Ratan"
        self.marks=800

    def introduce(self): ##this type methos "introduce(self)" called instance methods and here is introduce 
        print("Roll is: ",self.roll)
        print("Name is: ",self.name)
        print("Marks is: ",self.marks)

s1= Student()
s1.introduce()
'''

'''
class Song:
    """This is the Song class with required data and behaviour"""
    
    def __init__(self, artist, title):
       print("inside the constructor")
       self.artist = artist
       self.title=title

    def play(self):
        print("{0} is singing {1}".format(self.artist, self.title))



s1 = Song("Lata", "Wande Matram") ##s1 is reference variable of your object
s1.play()

s2 = Song("Shukwindar", "Jai Ho") ##s2, s1 is reference variable but line. 51 & 52 artist and title is instance variable
# s2.play()
s2.artist = "B Prak"
s2.title = "Teri Mitti"
s2.play()

'''

##instance variable

''' FIRST METHOD
class Employee:
    def __init__(self):
        self.empId=10
        self.empName="Ram"
        self.salary=80000


emp1 = Employee()

print(emp1.__dict__)
'''

''' SECOND METHOD
class Demo:
    def __init__(self):
        self.a=10
        self.b=20

    def fun1(self):
        print("inside fun1 method of Demo class")
        self.c=30

d1 = Demo()

print(d1.__dict__) # {'a': 10, 'b': 20}

d1.fun1() # inside fun1 method of Demo class

print(d1.__dict__) # {'a': 10, 'b': 20, 'c': 30}

d1.d = 50
print(d1.__dict__) 

d2= Demo()
d2.x=1000
print(d2.__dict__) 
'''
#Deleting an instance variable:

'''
class Demo:
    def __init__(self): #4 instance variable
        self.a=10
        self.b=20
        self.c=30
        self.d=40

    def fun1(self): #instance method is fun1
        print("inside fun1 method of Demo class")
        print("deleting the variable d")
        del self.d


d1 = Demo()

print(d1.__dict__)
d1.fun1()
print(d1.__dict__)
del d1.c
print(d1.__dict__)

#things change now.
d2 = Demo()
print(d2.__dict__)
'''

'''
class Demo:
    def __init__(self):
        self.x=10
        self.y=20


d1 = Demo()

d1.x=100
d1.y=200

print(d1.x)
print(d1.y)

d2 = Demo()

print(d2.x) 
print(d2.y)
'''


class Demo:
    def __init__(self):
        self.x=10
        self.y=20



d1 = Demo()

d2 = d1

d1.x=100
d1.y=200

print(d1.x)
print(d1.y)

print(d2.x)
print(d2.y)