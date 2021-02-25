# Problem:
# Given an nxn two-dimensional array and a score for each cell, print the maximum score that can be obtained in the mxm area.

# My Solution:
T = int(input())
for i in range(T):
    N, M = map(int, input().split())

    print("#{}".format(i + 1), end=" ")
    board = []
    for j in range(N):
        board.append(list(map(int, input().split())))

    maximum = 0
    for j in range(N - M + 1):
        for k in range(N - M + 1):
            tot = 0
            for l in range(j, j + M):
                tot += sum(board[l][k:k + M])
            if tot > maximum:
                maximum = tot
    print(maximum)
