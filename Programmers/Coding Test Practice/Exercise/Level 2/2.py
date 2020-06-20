# Problem:
# Given a board, return the maximum space of square of 1s.

# My Solution:
def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                answer = 1

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 0:
                continue
            else:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                if board[i][j] > answer:
                    answer = board[i][j]

    return answer * answer
