# String is a built in data type that store sequence of characters.The sequence of characters is enclosed within single,double,triple quotes
#To swap multiline string alwasys use single triple quotes , and if you are using post office in string then do not single quotes
a="coder"# string
b='coder'#string
c='''coder'''#string
print("twinkle twinkle little star
      how are wonder what you are")# will throw syntax error reason is swap  multiline only by using triple single qoutes 
print('my father's')# will throw syntax error you have to use here double quotes
# concatenation is a operation to add two or more string
name =input("enter your name:") 
print("goodmorning"+name)
# len()-it is a function to retrieve number of characters in a string
x="coder"
print(len(x))
#Indexing - it is used to retrieve character from string
x="Tamanna Dahiya" # consider space  a one character
print(x[0])
print(x[1])
x[1]="h"#throw type error as string ius immutable data type
#Slicing-It is used to fetch a part of string
x="Tamanna Dahiya" # consider space  a one character
print(x[1:4])#will exclude upper limit
# some other functions let's first discuss first function endswith
print(x.endswith("ya"))# return answer either true or false
#capitalize ()-will convert first letter to upper case
x="tamanna Dahiya" # consider space  a one character
x.capitalize()
print(x)
# replace()-will repalce character from string to another character
x.replace("a","c")
print(x)
# find()-will retrieve index of given character of first occurence
x.find("a")
print(x)
#count()-will tell the number of times a character comes in a string
x.count("a")
print(x)
#Escape sequence characters starting with backslash followed with one or more chacters generally used for formatting
#/a-beep sound 
#/n-new line
#/t-tab space
#/a,/n,/t considered to be single character
