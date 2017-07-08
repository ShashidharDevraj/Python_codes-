


'''
def dict_2_list(d):
    c = list(d)   # This will print all the keys in list 
 
    for i in c:
        c.append(d[i])
    

d = {'a':1, 'b':2,'c':5,'g':6,'u':9}    
print dict_2_list(d)
'''


# Working code
d = {'a':1, 'b':2,'c':5,'g':6,'u':9}

a = d.keys()
b = d.values()

for i in b:
    a.append(i)

print a 


