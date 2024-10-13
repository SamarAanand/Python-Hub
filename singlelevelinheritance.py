#inheritance is the ability of class to inherit the methods and functions of already existing class
#basic syntax class name of derived class (name of parent class):
# derived/sub class is one which inherits the function and methods while parent/super/base class is exixting class of which functions and methods are inherited
class Human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class girl(human):
g1=girl()
x=g1.eat()
print(x)