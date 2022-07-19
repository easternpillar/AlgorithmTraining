# Reference: https://www.acmicpc.net/problem/14499
import sys
from collections import deque

N, M, x, y, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dice_vertical = deque([0, 0, 0, 0])
dice_horizontal = deque([0, 0, 0])

for command in list(map(int, sys.stdin.readline().split())):
    if command == 1 and y + 1 < M:
        y += 1
        temp1 = dice_horizontal.pop()
        temp2 = dice_vertical.pop()
        dice_horizontal.appendleft(temp2)
        dice_vertical.append(temp1)
        dice_vertical[1] = dice_horizontal[1]
        if board[x][y] == 0:
            board[x][y] = dice_vertical[-1]
        else:
            dice_vertical[-1] = board[x][y]
            board[x][y] = 0
        print(dice_vertical[1])
    elif command == 2 and y - 1 >= 0:
        y -= 1
        temp1 = dice_horizontal.popleft()
        temp2 = dice_vertical.pop()
        dice_horizontal.append(temp2)
        dice_vertical.append(temp1)
        dice_vertical[1] = dice_horizontal[1]
        if board[x][y] == 0:
            board[x][y] = dice_vertical[-1]
        else:
            dice_vertical[-1] = board[x][y]
            board[x][y] = 0
        print(dice_vertical[1])
    elif command == 3 and x - 1 >= 0:
        x -= 1
        dice_vertical.append(dice_vertical.popleft())
        dice_horizontal[1] = dice_vertical[1]
        if board[x][y] == 0:
            board[x][y] = dice_vertical[-1]
        else:
            dice_vertical[-1] = board[x][y]
            board[x][y] = 0
        print(dice_vertical[1])
    elif command == 4 and x + 1 < N:
        x += 1
        dice_vertical.appendleft(dice_vertical.pop())
        dice_horizontal[1] = dice_vertical[1]
        if board[x][y] == 0:
            board[x][y] = dice_vertical[-1]
        else:
            dice_vertical[-1] = board[x][y]
            board[x][y] = 0
        print(dice_vertical[1])
    else:
        continue