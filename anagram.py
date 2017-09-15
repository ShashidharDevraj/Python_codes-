# Script to check the given string is anagram or not.

a = 'chaitanya'
b = 'achintya'


l = len(a)

for i in range(l):
    if a[i] not in b:
        print ("the given strings are not an anagram")
        break
else:
    print ("the given strings are an anagram")







