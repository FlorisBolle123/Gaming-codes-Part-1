sample_list=[1,1,2,2,3,3,4,4,]

#convert a list into a set
sample_set=set(sample_list)
print(sample_set)

if 4 in sample_set:
    print("yes")
else:
    print("no")

#This is the only way you can create a empty set
myset=set([])

myset.add(4)
myset.add(6)
myset.add(5)
myset.add(4)
myset.add(2)
myset.add(3)
myset.add(1)

print(myset)

#use discard instead of remove beacause remove removes it from the list but discard ignores the value you have entered
myset.discard(7)
myset.discard(2)

print(myset)

"""
set operations
1- union
means addition of sets
2- interaction
common elements of sets
3- difference
4- symmetric difference
"""
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}

#union
print(a|b)

#interaction
print (a & b)

#difference
print(b-a)

#symmetric difference
print (a^b)