# Fibinacci series.
# The below code becomes slower after 35. since the processing time is huge.

def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
  	return fib(x-1) + fib(x-2)   # recursion process. Ex: fib(2-1) + fib(2-2)

print(fib(35))


# Memoization: This concept helps in caching the previous values. 
# Using the below method you can go for maximum range.

fib_dic = {}
def fibi(n):
	if n in fib_dic:
		return fib_dic[n]
	if n in (1,2):
		value = 1
	elif n > 2:
		value = fibi(n-1) + fibi(n-2)
	fib_dic[n] = value              # Storing the number and its value in a dictionary.
	return value


for i in range(1,1001):
	print(i,":", fibi(i))



# Another way to solve Fibinacci series is utilizing the  
# existing decorator.

from functools import lru_cache

@lru_cache(maxsize=1000)   # Mention the maxsize to cash. By default it is 128bytes.
def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
  	return fib(x-1) + fib(x-2)


for i in range(1,1000):
	print(fib(i))


