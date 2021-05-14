# Problem:
# Reference: https://www.acmicpc.net/problem/17829

# My Solution:
import sys


def DnC(b):
    length = len(b)
    if length == 2:
        temp = []
        for eli in b:
            temp.extend(eli)
        return sorted(temp, reverse=True)[1]

    b1 = []
    b2 = []
    b3 = []
    b4 = []
    for i in range(length // 2):
        b1.append(b[i][:length // 2][:])
        b2.append(b[i][length // 2:][:])
    for i in range(length // 2, length):
        b3.append(b[i][:length // 2][:])
        b4.append(b[i][length // 2:][:])

    temp = [DnC(b1), DnC(b2), DnC(b3), DnC(b4)]
    return sorted(temp, reverse=True)[1]


N = int(sys.stdin.readline().rstrip())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

print(DnC(board))
