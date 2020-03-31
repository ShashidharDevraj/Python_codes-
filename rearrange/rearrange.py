# Script to read a text file and print the date present 
# at first position at the last.

# Input = "31.3.2020 corona is going wild"

# Output = "corona is going wild 31.3.2020"

with open("rearrange.txt") as f:
	for words in f.readlines():
		arr = words.split()
		# print(arr)
		arr.append(arr[0])
		arr.remove(arr[0])
		print(" ".join(arr))





