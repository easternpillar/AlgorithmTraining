# Problem:
# Use the star (*) character to print a rectangle shape with a length of n and a length of m.

# My Solution:
a, b = map(int, input().strip().split(' '))

for i in range(b):
    print('*'*a)