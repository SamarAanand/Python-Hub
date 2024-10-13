# Basic syntax of while loop
'''while condition:
    body of block'''
# Body of block will execute only if condition is true
#program to print number from 1 to 10
i=1
while i<=10:
    print(i)
    i=i+1
# program to print yes 5 times    
i=1
while i<=5:
    print("yes")
    i=i+1
# program to print table of  number using while loop
num=int(input("enter a number:"))
i=1
while i <=10:
    print(num*i)
    i=i+1
# using  while loop print all content of list
l=["apple","mangoes","banana","orange","guava"]
i=0 
while i<len(l):
    print(l[i])
    i=i+1

    