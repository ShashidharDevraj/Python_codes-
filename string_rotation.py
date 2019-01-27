# Script to rotate a given string to left/right.


def rotate_left(input, d):
    L1 = input[0: d]
    L2 = input[d:]
    return("Left rotation : ", (L2 + L1))


def rotate_right(input, d):
    R1 = input[0: len(input) - d]
    R2 = input[len(input) - d:]
    return("Right rotation : ", (R2 + R1))


input = 'shashi'
d = 4
print(rotate_left(input, d))
print(rotate_right(input, d))
