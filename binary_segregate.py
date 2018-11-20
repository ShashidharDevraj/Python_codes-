# script to adjust the '1' to one side and '0' to another side

bin = '0011010101001'

a = []
count = 0  
for i in bin:
	if i == '1':
		a.append(i)
	else:
		count +=1

a.append('0' * count)
print(''.join(a))
