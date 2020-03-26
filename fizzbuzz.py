# Script to print the "Fizz" if given number is divisible by 3
# "Buzz" if number is divisible by 5
# "FizzBuzz" if number is divisible by both 3 and 5 


def fizzbuzz(num):
	for i in range(1,num+1):
		if i%3 == 0 and i%5 == 0:
			print("FizzBuzz")
		elif i%3 == 0:
			print("Fizz")
		elif i%5 == 0:
			print("Buzz")
		else:
			print(i) 


fizzbuzz(15) 