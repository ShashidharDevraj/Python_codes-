# script to check the character count.

def character_count(a):
    d = {}
    count = 1
    for i in a:
        if i not in d:
            d[i] = count
        else:
            d[i] += 1
    return d

if __name__ == '__main__':
    a = 'achintyaa'
    b = 'chaitanya'
    print (character_count(a))
    print (character_count(b))

    if character_count(a) == character_count(b):
        print ("its an anagram")
    else:
        print ("not an anagaram")


