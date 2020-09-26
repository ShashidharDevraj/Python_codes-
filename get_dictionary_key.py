# Script to get the key by providing the value from a given dictionary

my_dict = {'java': 100, 'python':112, 'cpython':11}

key_list = list(my_dict.keys())
value_list = list(my_dict.values())

print(key_list[value_list.index(100)])


print(list(my_dict.keys())[list(my_dict.values()).index(112)])
# OR
print() 
print(list(my_dict.values()).index(11))
print(list(my_dict.keys())[2])


# Output
#---------
java
python

1
cpython
