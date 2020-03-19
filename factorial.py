def factorial(num):
	fact = 1
	if num < 0:
		print("Enter positive number.")
	elif num == 0:
		print("The factorial of O is 1.")
	else:
		for i in range(1, num+1):
			fact = fact * i
			print(fact)

number = 5
factorial(number)