# Set is collection of unique elements.it is enclosed within curly brackets .it is unordered ,unindexed,mutable,cannot contain duplicate elements
# program to create empty set
#s={}-completely wrong as it is not set it is a dictionary
s=set()# correct way to make an empty set
s.add(1)
s.add(2)
s.add(3)
s.add(2)
s.add(2)
print(s)# will give only 1,2,3 automatically removes duplicate element
'''very very important question for interview purpose
set is mutable or immutable data type
so,set is mutable as we have seen above we are able to add element in an empty set 
and elements of set are immutable '''
# let's discuss some of the functions of set
#pop():will remove any random element from set
s.pop()
print(s)
# remove()-it will remove element of your choice
s.remove(2)
# clear()- will empty set
s.clear()
print(s)
s1={5,6,7,8,9}
#union()-will combine elements of two sets
s1.union({2,3})
print(s1)
#intersection()-will take common elements of two sets
s1.intersection({3,5})
print(s1)