#Variable is a name given to memory location in a program. In simple words it is a container that stores value
a=2 #Data type-int(Integer)
b="Tamanna"#Data type-str(String)
c=20.0#Data type-Float
d=None#Data type-None
e=False#Data type-bool(Boolean)
print(a)
print(b)
print(c)
print(d)
print(e)
#To check data type of any variable we use type()
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# operators are special symbols which performs operation on operands
#Arithmetic operators are those which perform mathetical operations(+,-,*,/,//,**)
x=45
y=56
z=34
print(x+y)
print(y-z)
print(x*y)
print(x/y)# always return float value
print(x//y)#floor division also return integer value
print(x**y)#It will return x raised to power y
# relational operators are used to compare(<,>,<=,>=,==(equalto),!=(not equal to),these operators always return answer in true or false)
print(x<y)
print(y>z)
print(x==y)
print(x!=y)
print(x<=z)#less than or equal to
print(x>=y)#greater than or equal to
#assignment operators used to assign values to variables(=,+=,-=,*=,/=)
num=3
num+=6
print(num)
num-=5
print(num)
num*=4
print(num)
# logical operators(and,or,not)
'''In case of and
true and true-true
false and false-false
true and false-false
false and true-false'''
print(3<4 and 7>8)
print(5>6 and 5<6)
'''in case of not 
not true-false
not false-true'''
print(not 5>6)
print(not 6<8)
'''in case of or
true or true-true
false or false-false
true or false-true
false or true-true'''
print(45<45 or 56<89)
# type conversion is basically conversion of data type from one data type to another automatically by a interpreter
a=2
b=3.0
print(a+b)# here 2 will be converted to 2.0 automatically by  an interpreter because flost data type is consisdered to be superrior as compared to integer
x="20"
y=20
print(x+y)# will throw type error as we are adding string to integer
# to get its output we have to change string to integer and for that we have to use type casting in which data type is manually converted
x=int("20")
y=20
print(x+y)# now we will get output 
# one very important point
print(type(int("coder")))# will throw value error we cannot convert sequence of characters to integer by type casting
# input fu(nction is used to accept the value from user and until and unless we use type casting
name=input("enter your name:")
num=input("enter a number:")# it will a string to make it int use type casting
num=int(input("enter a number:"))
