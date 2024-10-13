# you might have learn the concept of factorial in maths 5!=5*4*3*2*1=120
# but today let's write a program to find factorial of a number using procedural and functional programming
num=int(input("enter a number:"))
if num==0:
    print("factorial of 0 is :",1)
elif num==1:
    print("factorial of 1 is:",1)
else:
    fact=1
    for i in range(1,num+1):
        factorial=fact*num+1
print(factorial)               