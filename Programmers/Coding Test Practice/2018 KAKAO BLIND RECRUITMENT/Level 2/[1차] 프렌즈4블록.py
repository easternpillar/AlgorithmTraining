# Problem:
# Given a board, return the number of erased blocks.
# Condition(s):
# 1. Remove the 2x2 blocks if they have the same value.
# 2. Align down after the elimination.

# My Solution:
def solution(m, n, board):
    answer = 0
    board = list(map(list, board))

    while True:
        flag = 0
        eli = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0 and board[i][j] == board[i][j + 1] and board[i][j] == board[i][j + 1] and board[i][
                    j] == board[i + 1][j] and board[i][j] == board[i + 1][j + 1]:
                    eli.add((i, j))
                    eli.add((i, j + 1))
                    eli.add((i + 1, j))
                    eli.add((i + 1, j + 1))
                    flag = 1

        for x, y in eli:
            board[x][y] = 0

        for i in range(m - 1, 0, -1):
            for j in range(n):
                if board[i][j] == 0:
                    idx = i - 1
                    while idx >= 0:
                        if board[idx][j] != 0:
                            board[i][j] = board[idx][j]
                            board[idx][j] = 0
                            break
                        idx -= 1
        answer += len(eli)
        if flag == 0:
            break

    return answer
