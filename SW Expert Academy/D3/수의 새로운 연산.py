# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV2b-QGqADMBBASw&categoryId=AV2b-QGqADMBBASw&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=7

# My Solution:
import bisect


def pos(value):
    global seq
    temp = bisect.bisect(seq, value)
    col = temp - (value - seq[temp - 1])
    row = value - seq[temp - 1] + 1
    return row, col


def value(x, y):
    global seq
    return seq[x + y - 2] + x - 1


seq = [1]
for i in range(1, 10000):
    seq.append(seq[-1] + i)

answer = []
for i in range(int(input())):
    p, q = map(int, input().split())

    x1, y1 = pos(p)
    x2, y2 = pos(q)
    x, y = x1 + x2, y1 + y2
    answer.append(value(x, y))

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
