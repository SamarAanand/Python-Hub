# function is a block of statement that perform specific task
#program to define a function which calculate sum of two numbers
def sum(a,b): #function definition
    return a+b
x=sum(34,56)# function call
print(x)
#program to define a function which find average of three numbers
def avg(a,b,c):
    return (a+b+c)/3
x=avg(1,3,4)
print(x)
#program by which we can give default parameters
def sum(a=5,b=3): #function definition with default parameters
    return a+b 
x=sum()# function call without any parameters
print(x)
# function take input and return output ,if we will not give any parameters then it will return none
# built in function -print()
print("Tamanna",end=" ")
print("Dahiya")  
# when a function call itself repeatedly then it is called recursion
def show(n):
    return n
x=show(5)
print(x)
# this above code will return me only 5 but we want 5,4,3,2,1 we can use loops but if we want to do it by recursions we can do it
def show(n):
    if n==0: #base condition necessary to give in recursions
        print(n) 
    show(n-1)
show(5)
    