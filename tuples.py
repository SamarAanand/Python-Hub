# Tuple is an immutable data type 
# it is enclosed by round brackets
t=([1,2],3)
# indexing as same concepts as we discussed in strings and list
print(t[0])
t[0]=1#not possible to do this as tuple is immutable ,it will throw type error
# wap to create an empty tuple
t=()
# to create a tuple of single element
t=(1,)# comma after this 1 is necessary if this is not given and if you will fetch its type then it will come integer
t=(2)
print(type(t))# int
# now let's discuss the methods of tuple
#find()- it will give you the index of first occurence of an elemnet in tuple if elemnet does not exist then value error will come
t1=(1,2,3,4,3,2)
t1.find(2)
print(t1)
#count()-it will tell how many times an element comes in tuple if element does not exist then it will give 0
t1.count(2)
print(t1)