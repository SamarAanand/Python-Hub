# conditional statements are those statements which are executed when the condition sets to be true
''' for example if i say if the day is sunny i am going to order an icecream so this task is possible only if conditio is true
similarly in python programming there are some statements which will only execute of condition sets to be true'''
# simple syntax of if-else
a=3
b=6
c=9
if a<b:# in this code if condition of if is true than statement of if will be exceuted and if condition of if is false than statement of else will executed
    print("a is lesser than b")
else:
    print("a is greater than b")    
# if-elif-else 
if a>b:
    print("a is greater than b")
elif b<c:
    print("b is lesser than c")
else:
    print("none")
# one important tip - think as many possibilities you can try to execute that that will helps you in understanding this concept
'''in if-elif-else ladder first if condition of if is true then it's statement is executed and program will terminate
and if conditon is false then condition of elif will be checked if sets to true that will be exceuted and program terminates if not then it moves to else'''
# multiple if statements(multiple if statement will execute independently)")
if a<b:
    print("a is lesser than b")
if a<c:
    print("a is lesser than c")
if b<c:
    print("b is lesser than c")
elif c<b:
    print("c is lesser than b")
else:
    print("ok")                
# multiple elif statement and it will not execute independently
if a<b:
    print("a is lesser than b")
elif b<c:
    print("b is lesser than c")
elif a<c:
    print("a is lesser than c")
elif c<a:
    print("c is lesser than a")
else:
    print("ok")s                

           
