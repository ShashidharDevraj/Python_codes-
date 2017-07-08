# Script to find the missing items from the list 


def missing_items(*a):
    print "Actual list is :", a
    b = range(0,15)
    	
    a = set(a)
    b = set(b)
    c = a^b
    return c 


if __name__ == "__main__":
    a = [1,2,3,5,7,9,13] 
    #m = missing_items(1,2,3,5,7,9,13)
    m = missing_items(*a)
    print "Missing items from the list:",m




# Example to use *args

'''
def sum(*args):
    s = 0 
    for i in args:
        s +=i
    print ("sum is", s)


sum(1,2,3,5,6)

'''

'''
def my_three(a, b, c):
    print(a, b, c)
 
a = [1,2,3]
my_three(*a) # here list is broken into three elements
'''



# Example for **kwargs

'''
def my_func(**kwargs):
    for i, j in kwargs.items():
        print(i,j)

my_func(name='tim', sport='football', roll=19)
'''

"""
def my_three(a,b,c):
    print(a,b,c)
 
a = {'a': "one", 'b': "two", 'c': "three" }
my_three(**a)
"""
