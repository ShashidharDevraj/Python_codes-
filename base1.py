# script to find the count of vowels

def vowels(name):
    count = 0
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    
    for i in name:
        if i in vowels: 
            count +=1 
        
    return count


word = input()
x = vowels(word)
print(x)


# script to adjust the '1' to one side and '0' to another side

bin = '00111111'

a = []
count = 0  
for i in bin:
	if i == '1':
		a.append(i)
	else:
		count +=1

a.append('0' * count)
print(''.join(a))
