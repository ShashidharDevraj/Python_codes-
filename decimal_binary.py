# Decimal to Binary Conversion

def decimal_binary(n):
	if n >= 1:
		decimal_binary(n//2)
	print(n%2, end='')

n = 9
d = decimal_binary(n)



