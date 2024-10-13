# Dictionary is a datatype that stores key value pair.it is storewd in curly brackets{}
'''dictionary is mutable,unordered,indexed but can't contain duplicate keys'''
d={"name":"tamanna","course":"btechcse","year":1}# if you give duplicate keys in a dictionary then you will get name error 
#to access values by using keys
 print(d["name"])#if you committ some error in name of keys then you will get key error
# to create an empty dictionary
d={}
# to add keys in empty dictionary
d["name"]="Tamanna Dahiya "
d["profession"]="student"
print(d)
#Nested dictionary -in simple words nested dictionary means a dictionary within another dictionary
d1={"a":{"b":2},"d":3}
# you can also give list or tuple as a value in dictionary
# one most important point-in a dictionary two values can be same but two keys cannot
# now let's discuss some of the most important methods of dictionary
#first is .keys()-it will give you all the keys present in a dictionary(keys will be given in list)
print(d.keys())
# .values()-it will give you all the values of dictionary( values will be given in list)
print(d.values())
#.items()-ot will give combination of key and value pair in tuple
print(d.items())
#.get() -its work will be similar to this (print(d["name"])
#but the benefit of using .get is if you give wrong name of key then it will give none 
print(d.get("name")) 
# last method which we will discuss is that .update()
d.update({"me":"learner"})
print(d)
