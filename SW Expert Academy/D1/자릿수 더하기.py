# Problem:
# Write a program that takes one natural number and calculates the sum of each digit.

# My Solution:
N = input()
total = 0

for i in range(len(N)):
    total += int(N[i])
print(total)