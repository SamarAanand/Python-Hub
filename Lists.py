#List is data type that stores a set of values of different data type
l=[1,2.0,3,"4"]
#indexing and slicing as discussed in strings apply same concept in list as well
print(l[0])
print(l[2])
l[2]=4 # possible as list is mutable data type but we can not do this in strings
print(l)
# some functions regarding list 
#let's discuss first function sort() that will arrange the list in incresing order
print(l.sort())# will throw none to get output you have to store this in other variable 
l=l.sort()
print(l)
# to arrange elements of list in decreasing order use sort(reverse=True)
l=l.sort(reverse=True)
print(l)
# to reverse the list use reverse()
l=l.reverse()
print(l)
#append()-it is used to add an ele,ent in the end of list
l.append(4)
print(l)
# to add an element at specifird index we use insert(index,element)
l.insert(2,5)
print(l)
# remove() is used to remove en element(in paranthesis you are supposed yo give element which you want to remove)
l.remove(4)
print(l)
# pop()-it is used to remove element from list which is at given index
l.pop(1)
print(l)