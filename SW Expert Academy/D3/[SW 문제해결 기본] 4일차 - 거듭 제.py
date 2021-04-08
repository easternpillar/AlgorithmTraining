# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14dUIaAAUCFAYD&categoryId=AV14dUIaAAUCFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9

# My Solution:
import math

answer = []
for i in range(10):
    tn = int(input())
    a, r = map(int, input().split())
    answer.append(int(math.pow(a, r)))

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))

# Other Solution:
# def pow(a, m, r):
#     if r == 1:
#         return m
#     else:
#         return pow(a, a * m, r - 1)
#
#
# answer = []
# for i in range(10):
#     tn = int(input())
#     a, r = map(int, input().split())
#     answer.append(pow(a, a, r))
#
# for i in range(len(answer)):
#     print("#{} {}".format(i + 1, answer[i]))
