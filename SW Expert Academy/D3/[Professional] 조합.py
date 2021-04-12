# Problem:
# Print the N combination R value.

# My Solution: Denied.
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
# def combination(n, r):
#     return factorial(n) / factorial(r) / factorial(n - r)
#
#
# answer = []
# for i in range(int(input())):
#     N, R = map(int, input().split())
#     answer.append(int(combination(N, R)) % 1234567891)
#
# for i in range(len(answer)):
#     print("#{} {}".format(i + 1, answer[i]))

# def combination(n,r):
#     if n==r:
#         return 1
#     elif r==1:
#         return n
#     else:
#         return combination(n-1,r-1)+combination(n-1,r)
#
# answer=[]
# for i in range(int(input())):
#     N,R=map(int,input().split())
#     answer.append(combination(N,R)%1234567891)
#
# for i in range(len(answer)):
#     print("#{} {}".format(i+1,answer[i]))
import math


def divpow(num, p):
    global MOD
    if p == 0:
        return 1
    elif p == 1:
        return num
    if p % 2 == 0:
        temp = divpow(num, p / 2)
        return (temp * temp) % MOD
    temp = divpow(num, p - 1) % MOD
    return (temp * num) % MOD


answer = []
MOD = 1234567891
factorial = [0 for _ in range(1000001)]
factorial[0] = 1
for i in range(1, len(factorial)):
    factorial[i] = (factorial[i - 1] * i) % MOD

for i in range(int(input())):
    N, R = map(int, input().split())
    up = factorial[N]
    down = divpow((factorial[N - R] * factorial[R]) % MOD, MOD - 2)
    answer.append((up * down) % MOD)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
