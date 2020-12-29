# Problem:
# Given a string of length 30, print the length of the repeated word.
# Condition(s):
# 1. The length of the word is at most 10.

# My Solution:
T = int(input())
for i in range(T):
    temp = input()
    length = 1
    while length <= 10:
        word = temp[:length] * 30
        if word[:30] == temp:
            print("#{} {}".format(i + 1, length))
            break
        else:
            length += 1
