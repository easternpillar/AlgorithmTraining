# Reference: https://www.acmicpc.net/problem/13460
import heapq
import sys
from copy import deepcopy


def left(board, red, blue):
    # print("left")
    red_new = red[:]
    blue_new = blue[:]
    if red[1] < blue[1]:
        board[red[0]][red[1]] = '.'
        while red_new[1] > 0:
            if board[red_new[0]][red_new[1] - 1] == '.':
                red_new[1] -= 1
            elif board[red_new[0]][red_new[1] - 1] == 'O':
                red_new[1] -= 1
                board[red[0]][red[1]] = '.'
                break
            else:
                board[red_new[0]][red_new[1]] = 'R'
                break
        board[blue[0]][blue[1]] = '.'
        while blue_new[1] > 0:
            if board[blue_new[0]][blue_new[1] - 1] == '.':
                blue_new[1] -= 1
            elif board[blue_new[0]][blue_new[1] - 1] == 'O':
                blue_new[1] -= 1
                board[blue[0]][blue[1]] = '.'
                break
            else:
                board[blue_new[0]][blue_new[1]] = 'B'
                break
    else:
        board[blue[0]][blue[1]] = '.'
        while blue_new[1] > 0:
            if board[blue_new[0]][blue_new[1] - 1] == '.':
                blue_new[1] -= 1
            elif board[blue_new[0]][blue_new[1] - 1] == 'O':
                blue_new[1] -= 1
                board[blue[0]][blue[1]] = '.'
                break
            else:
                board[blue_new[0]][blue_new[1]] = 'B'
                break
        board[red[0]][red[1]] = '.'
        while red_new[1] > 0:
            if board[red_new[0]][red_new[1] - 1] == '.':
                red_new[1] -= 1
            elif board[red_new[0]][red_new[1] - 1] == 'O':
                red_new[1] -= 1
                board[red[0]][red[1]] = '.'
                break
            else:
                board[red_new[0]][red_new[1]] = 'R'
                break
    # for b in board:
    #     print(b)
    return (deepcopy(board), red_new, blue_new)


def right(board, red, blue):
    # print("right")
    red_new = red[:]
    blue_new = blue[:]
    if red[1] > blue[1]:
        board[red[0]][red[1]] = '.'
        while red_new[1] < len(board[0]) - 1:
            if board[red_new[0]][red_new[1] + 1] == '.':
                red_new[1] += 1
            elif board[red_new[0]][red_new[1] + 1] == 'O':
                red_new[1] += 1
                board[red[0]][red[1]] = '.'
                break
            else:
                board[red_new[0]][red_new[1]] = 'R'
                break
        board[blue[0]][blue[1]] = '.'
        while blue_new[1] < len(board[0]) - 1:
            if board[blue_new[0]][blue_new[1] + 1] == '.':
                blue_new[1] += 1
            elif board[blue_new[0]][blue_new[1] + 1] == 'O':
                blue_new[1] += 1
                board[blue[0]][blue[1]] = '.'
                break
            else:
                board[blue_new[0]][blue_new[1]] = 'B'
                break
    else:
        board[blue[0]][blue[1]] = '.'
        while blue_new[1] < len(board[0]) - 1:
            if board[blue_new[0]][blue_new[1] + 1] == '.':
                blue_new[1] += 1
            elif board[blue_new[0]][blue_new[1] + 1] == 'O':
                blue_new[1] += 1
                board[blue[0]][blue[1]] = '.'
                break
            else:
                board[blue_new[0]][blue_new[1]] = 'B'
                break
        board[red[0]][red[1]] = '.'
        while red_new[1] < len(board[0]) - 1:
            if board[red_new[0]][red_new[1] + 1] == '.':
                red_new[1] += 1
            elif board[red_new[0]][red_new[1] + 1] == 'O':
                red_new[1] += 1
                board[red[0]][red[1]] = '.'
                break
            else:
                board[red_new[0]][red_new[1]] = 'R'
                break
    # for b in board:
    #     print(b)
    return (deepcopy(board), red_new, blue_new)


def up(board, red, blue):
    # print("up")
    red_new = red[:]
    blue_new = blue[:]
    if red[0] < blue[0]:
        board[red[0]][red[1]] = '.'
        while red_new[0] > 0:
            if board[red_new[0] - 1][red_new[1]] == '.':
                red_new[0] -= 1
            elif board[red_new[0] - 1][red_new[1]] == 'O':
                red_new[0] -= 1
                board[red[0]][red[1]] = '.'
                break
            else:
                board[red_new[0]][red_new[1]] = 'R'
                break
        board[blue[0]][blue[1]] = '.'
        while blue_new[0] > 0:
            if board[blue_new[0] - 1][blue_new[1]] == '.':
                blue_new[0] -= 1
            elif board[blue_new[0] - 1][blue_new[1]] == 'O':
                blue_new[0] -= 1
                board[blue[0]][blue[1]] = '.'
                break
            else:
                board[blue_new[0]][blue_new[1]] = 'B'
                break
    else:
        board[blue[0]][blue[1]] = '.'
        while blue_new[0] > 0:
            if board[blue_new[0] - 1][blue_new[1]] == '.':
                blue_new[0] -= 1
            elif board[blue_new[0] - 1][blue_new[1]] == 'O':
                blue_new[0] -= 1
                board[blue[0]][blue[1]] = '.'
                break
            else:
                board[blue_new[0]][blue_new[1]] = 'B'
                break
        board[red[0]][red[1]] = '.'
        while red_new[0] > 0:
            if board[red_new[0] - 1][red_new[1]] == '.':
                red_new[0] -= 1
            elif board[red_new[0] - 1][red_new[1]] == 'O':
                red_new[0] -= 1
                board[red[0]][red[1]] = '.'
                break
            else:
                board[red_new[0]][red_new[1]] = 'R'
                break

    # for b in board:
    #     print(b)
    return (deepcopy(board), red_new, blue_new)


def down(board, red, blue):
    # print("down")
    red_new = red[:]
    blue_new = blue[:]
    if red[0] > blue[0]:
        board[red[0]][red[1]] = '.'
        while red_new[0] < len(board) - 1:
            if board[red_new[0] + 1][red_new[1]] == '.':
                red_new[0] += 1
            elif board[red_new[0] + 1][red_new[1]] == 'O':
                red_new[0] += 1
                break
            else:
                board[red_new[0]][red_new[1]] = 'R'
                break
        board[blue[0]][blue[1]] = '.'
        while blue_new[0] < len(board) - 1:
            if board[blue_new[0] + 1][blue_new[1]] == '.':
                blue_new[0] += 1
            elif board[blue_new[0] + 1][blue_new[1]] == 'O':
                blue_new[0] += 1
                break
            else:
                board[blue_new[0]][blue_new[1]] = 'B'
                break
    else:
        board[blue[0]][blue[1]] = '.'
        while blue_new[0] < len(board) - 1:
            if board[blue_new[0] + 1][blue_new[1]] == '.':
                blue_new[0] += 1
            elif board[blue_new[0] + 1][blue_new[1]] == 'O':
                blue_new[0] += 1
                break
            else:
                board[blue_new[0]][blue_new[1]] = 'B'
                break
        board[red[0]][red[1]] = '.'
        while red_new[0] < len(board) - 1:
            if board[red_new[0] + 1][red_new[1]] == '.':
                red_new[0] += 1
            elif board[red_new[0] + 1][red_new[1]] == 'O':
                red_new[0] += 1
                break
            else:
                board[red_new[0]][red_new[1]] = 'R'
                break
    # for b in board:
    #     print(b)
    return (deepcopy(board), red_new, blue_new)


N, M = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

red = []
blue = []
dest = []
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == 'R':
            red = [i, j]
            continue
        if board[i][j] == 'B':
            blue = [i, j]
            continue
        if board[i][j] == 'O':
            dest = [i, j]
            continue
        if blue and red and dest:
            break

q = [(0, (deepcopy(board), red[:], blue[:]))]
heapq.heapify(q)
visited = set()
answer = -1

while q:
    cnt_pop, board_info = heapq.heappop(q)
    board_pop, red_pop, blue_pop = board_info
    if (tuple(red_pop), tuple(blue_pop)) in visited:
        continue

    # for b in board_pop:
    #     print(b)
    # print(cnt_pop)
    visited.add((tuple(red_pop), tuple(blue_pop)))
    if cnt_pop > 10:
        answer = -1
        break
    if blue_pop == dest:
        continue
    if red_pop == dest:
        answer = cnt_pop
        break

    heapq.heappush(q, (cnt_pop + 1, left(deepcopy(board_pop), red_pop, blue_pop)))
    heapq.heappush(q, (cnt_pop + 1, right(deepcopy(board_pop), red_pop, blue_pop)))
    heapq.heappush(q, (cnt_pop + 1, up(deepcopy(board_pop), red_pop, blue_pop)))
    heapq.heappush(q, (cnt_pop + 1, down(deepcopy(board_pop), red_pop, blue_pop)))
print(answer)
