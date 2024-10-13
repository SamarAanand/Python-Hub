# to open a file and to read content from it,python files are text files
f=open("tamanna.py","r")
data=f.read()#cannot be called again and again
print(data)
f.close()
# program to read only two characters of file(if we have not given any mode it will take red mode by default)
f=open("hello.py")
data=f.read(2)
print(data)
f.close()
# program tpo read first line of file
f=open("doubt1.py")
data=f.readline()
print(data)
f.close()
# program to write content in afile (we can use two modes one is write and another is append)
f=open("me.py","w")
f.write("python programming language")
f.close()
# best statemaent we can use to read or write is with statement because we need not to close the file
with open ("factorial.py") as f:
     data =f.read()
     print(data)