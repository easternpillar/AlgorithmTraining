# Problem:
# Write a program that takes 10 numbers and outputs the sum of only odd numbers.

# My Solution:
T = int(input())

for i in range(T):
    total = 0
    temp = list(map(int, list(input().split())))

    for num in temp:
        if num % 2 != 0:
            total += num

    print("#{} {}".format(i + 1, total))