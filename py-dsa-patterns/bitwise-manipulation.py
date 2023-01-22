# Example of bitwise manipulation pattern

a = 5
b = 6
a ^ b # 3
a & b # 4
a | b # 7
a << 1 # 10
a >> 1 # 2
a ^ 0 # 5
a ^ 1 # 4
a ^ a # 0
a ^ b ^ a # 6
a ^ b ^ b # 5

# XORing all elements of an iterable can be used to find the unique element in a list

def find_unique(arr):
    unique = 0
    for num in arr:
        unique ^= num
    return unique
