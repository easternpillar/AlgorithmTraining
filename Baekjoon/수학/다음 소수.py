# Problem:
# Reference: https://www.acmicpc.net/problem/4134

# My Solution:
import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    num = int(sys.stdin.readline().rstrip())
    if num <= 1:
        print(2)
        continue

    prime = num
    while True:
        flag = True
        for j in range(2, int(prime ** 0.5) + 1, 1):
            if prime % j == 0:
                flag = False
                break
        if flag:
            print(prime)
            break
        else:
            prime += 1
