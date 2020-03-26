# Python code to find the 3rd largest item in the given array. 
# Without using any sorting mechanism.
# This can be achived using a single loop.

def large(arr):
	max = 0
	largest = {}
	c = 1
	for i in arr:	
		if i > max:
			max = i
			largest[c] = i
			c +=1
	return di


arr = [65, 757, 95, 100, 45, 678, 999, 1010]
largest = large(arr)
print(largest)
length = len(largest)-2
print(largest[length])
