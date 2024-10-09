''' To map with real world situations we use objects.This is called is called object oriented programming .
     Class 8is blueprint for creating objects.The name of class shoud be given in pascal case.'''
# let's create a class and object
class Student:
    name="Tamanna Dahiya"
s1=Student() # paranthesis is used to call constructor
s2=Student()
print(s1)#it will tell that s1 is object of class student
print(s1.name)#print name    
print(s2.name)
#let's create one more class 
class Car:
    color="blue"
    brand="XYZ"
c1=Car() #c1 is an object 
c2=Car() 
print(c1.color)
print(c2.brand)
'''constructor__init__() will be called whenever a new object is initiated and if you have not defined constructor it will called automatically
   It will take an argument self you can give other argument as well other than self'''

''' There are two types of constructor-Default (it will have only argument self),parameterised is pone which has argument other than self'''
# let's write a code to define __init__()
class Student:
    name="Tamanna Dahiya"
    def __init__(self):
        print("Adding a new record to database")
s1=Student()
s2=Student()
print(s1.name)
print(s2.name)
#To give argument other than selg as well
class Car:
    def__init__(self,color,brand):
    self.color=color
    self.brand=brand
c1=Car("black","xyz")
c2=Car("white","abc")
print(c1.brend)
print(c1.color)    