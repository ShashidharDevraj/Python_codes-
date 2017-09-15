a = [-5, -7, -23, 0, 10,3,11, 0, 13,11]

ascend = []

while a:
	b = a[0]  
	for i in a:
		if i < b:       # '<' use this symbol to get the descending order.
			b = i
	ascend.append(b)
	a.remove(b)
print ascend

