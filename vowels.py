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
