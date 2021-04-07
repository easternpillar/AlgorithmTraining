# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8

# My Solution:
from collections import deque

answer = []
for i in range(10):
    N = int(input())
    encrypt = list(map(int, input().split()))
    q = deque(encrypt)

    add = 1
    while True:
        pop = q.popleft()
        if pop - add <= 0:
            q.append(0)
            break
        else:
            q.append(pop - add)
        add = add % 5 + 1

    answer.append(q)

for i in range(len(answer)):
    print("#{}".format(i + 1), end=" ")
    for j in range(len(answer[i])):
        print("{}".format(answer[i][j]), end=" ")
    print()
