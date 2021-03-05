# Problem:
# Given 5 lines of string, print the result of reading vertically.
# Condition(s):
# 1. The maximum length of a string is 15.

# My Solution:
T = int(input())
for i in range(T):
    board = []
    for j in range(5):
        temp = input()
        temp = temp.ljust(15, '#')
        board.append(temp.split()[0])
        board = list(map(list, board))

    print("#{}".format(i + 1), end=" ")
    for string in list(zip(*board)):
        for c in string:
            if c == '#':
                continue
            print(c, end="")
    print()
