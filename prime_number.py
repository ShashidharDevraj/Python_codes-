# Script to find the give number is prime or not. 
# Since i have used sys.argv here while running this python code run as "python prime_number.py <any number>"

import sys

def prime(num):
    # Checking the given number is greater than 1
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print (num,'is not a prime number..!!')
                print (i,'times',num//i,'is', num)
                break
        else:
            print (num,'is prime..!!!')
    else:
        print(num,'is not a prime number..!!')



if __name__ == '__main__':
    num = int(sys.argv[1])
    prime(num) 
