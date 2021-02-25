# Problem:
# Write a program that takes 10 numbers and outputs the average value.
# Condition(s):
# 1. The average is rounded to one decimal place.

# My Solution:
T = int(input())

for i in range(T):
    temp = list(map(int, list(input().split())))
    print("#{} {}".format(i + 1, round(sum(temp) / 10)))