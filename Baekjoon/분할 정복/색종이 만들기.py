# Problem:
# Reference: https://www.acmicpc.net/problem/2630

# My Solution:
import sys


def sum2d(array):
    tot = 0
    for i in range(len(array)):
        tot += sum(array[i])
    return tot


def divCon(board):
    global w, b
    summ = sum2d(board)
    if summ == 0:
        w += 1
    elif summ == len(board) * len(board):
        b += 1
    else:
        half = len(board) // 2
        b1 = []
        b2 = []
        b3 = []
        b4 = []
        for i in range(0, half):
            b1.append(board[i][:half])
            b2.append(board[i][half:])
        for i in range(half, len(board)):
            b3.append(board[i][:half])
            b4.append(board[i][half:])
        divCon(b1)
        divCon(b2)
        divCon(b3)
        divCon(b4)


w = b = 0
N = int(sys.stdin.readline().rstrip())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

divCon(board)
print(w)
print(b)
