# Problem:
# Given the othello game sequence, print the number of black and white stones.

# My Solution:
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def init(N):
    global board
    t_pos = N // 2
    board[t_pos - 1][t_pos - 1] = 2
    board[t_pos][t_pos] = 2
    board[t_pos][t_pos - 1] = 1
    board[t_pos - 1][t_pos] = 1


def isWall(x, y, color):
    global N, board
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    if not board[x][y]:
        return 0
    if board[x][y] == color:
        return 2
    return 1


def boardCheck(x, y, color):
    global board, dx, dy
    for i in range(8):
        d_x = dx[i]
        d_y = dy[i]
        change_list = []
        while True:

            a = isWall(x + d_x, y + d_y, color)

            if not a: break

            if a == 2:

                for c_x, c_y in change_list:
                    board[c_x][c_y] = color
                break

            if a == 1:
                change_list.append([x + d_x, y + d_y])
            d_x += dx[i]
            d_y += dy[i]
    board[x][y] = color


def w_b_count(N):
    global board, w_count, b_count
    for i in board:
        b_count += i.count(1)
        w_count += i.count(2)


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    init(N)
    for _ in range(M):
        x, y, color = map(int, input().split())
        boardCheck(x - 1, y - 1, color)

    w_count = 0
    b_count = 0
    w_b_count(N)

    print('#{} {} {}'.format(t, b_count, w_count))
