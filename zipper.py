# Given an input a and b of different length. Print an output as below
# Input: a = 'xyz'  
# Input: b = 'ABCD'
# Output: xAyBzCD

import itertools 

a = 'xyz'
b = 'ABCD'

n = list(itertools.zip_longest(a, b))

u = []
for i, j in n:
	u.append(i)
	u.append(j)

# print(u)

d = []
for r in u:
	if r is not None:
		d.append(r)
print("".join(d))
