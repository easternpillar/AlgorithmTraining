# Problem:
# Write a program that takes 10 numbers as input and outputs the largest number.

# My Solution:
T = int(input())
for i in range(T):
    print("#{} {}".format(i + 1, max(list(map(int, list(input().split()))))))
