# Binary to Decimal Conversion.

def binary_decimal(n):
	result = 0 
	length = len(n)-1
	for i in n:
		result += (int(i) * (2**length))
		length -=1
	return(result)


bin = '10101'
decimal = binary_decimal(bin)
print(decimal)