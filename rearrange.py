# Python code to rearrange the list as below using a single arr
# This code works for a list of numbers which are in serial
# with one number being positive and another being negative.

# Eg : # arr = [1,2,3,4,5,6,7,8,9,10,21,24,23,34]    # Works
# Eg : # arr = [1,2,3,4,5,6,7,8,14,16,9,10,21,24,23,34]   # Fails.

def method1(arr):
	even = 0 
	odd = 0 
	for i in arr:
		if i%2 == 0:
			even +=1
		else:
			odd +=1
	return even, odd


def method2(arr):
	even, odd = method1(arr)
	count = 0 
	for i in arr:
		if count < odd:
			if i%2 == 0:
				arr.remove(i)    # [1,3,5,7,9]
				arr.append(i)    # [2,4,6,8,10]
				count +=1
	return arr		

arr = [1,2,3,4,5,6,7,8,9,10]
m = method2(arr)
print(m)

