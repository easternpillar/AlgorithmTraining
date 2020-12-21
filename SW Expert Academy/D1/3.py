# Problem:
# Write a program that takes two numbers, compares the sizes, and outputs an equal or inequality sign.

# My Solution:
T = int(input())

for i in range(T):
    temp = list(map(int, list(input().split())))
    sign = ''
    if temp[0] > temp[1]:
        sign = '>'
    elif temp[0] == temp[1]:
        sign = '='
    else:
        sign = '<'

    print("#{} {}".format(i + 1, sign))
