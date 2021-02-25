# Problem:
# Fill a two-dimensional array from 1 to n*n by rotating inward clockwise.

# My Solution:
T = int(input())
for i in range(T):
    N = int(input())
    print("#{}".format(i + 1))

    board = [[0 for _ in range(N)] for _ in range(N)]

    value = 1
    r = 0
    c = -1
    while value <= N * N:
        while True:
            c += 1
            if c > N - 1 or board[r][c] != 0:
                c -= 1
                break
            board[r][c] = value
            value += 1
        while True:
            r += 1
            if r > N - 1 or board[r][c] != 0:
                r -= 1
                break
            board[r][c] = value
            value += 1
        while True:
            c -= 1
            if c < 0 or board[r][c] != 0:
                c += 1
                break
            board[r][c] = value
            value += 1
        while True:
            r -= 1
            if r < 0 or board[r][c] != 0:
                r += 1
                break
            board[r][c] = value
            value += 1

    for line in board:
        for b in line:
            print(b,end=" ")
        print("")
