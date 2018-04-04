# Script which helps in looping through the lists which are different in length. 

import itertools

name = ["raj", "john", "ruby", "niks"]

age = [10,20,30,40, 506]

colour = ["black", "brown", "white", "bluee", "green", "yello"]

origin = ["india", "us", "uk", "jp", "dubai", "nethreland", "nepal"]

location = ["Bangalore", "Mysore", "hydrabad", "UP"]

 
# For python2  
# for i, j, k, l, m  in itertools.izip_longest(name, age, colour, origin, location):
# 	print "%s %s %s %s %s" %(i,j,k,l,m)


# For python3 zip behaves as izip.
for i, j, k, l, m  in itertools.zip_longest(name, age, colour, origin, location):
	print("{} {} {} {} {}".format(i,j,k,l,m))