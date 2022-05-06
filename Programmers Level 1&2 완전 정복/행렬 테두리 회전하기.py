# 링크: https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3
# 문제 접근
# 1. 구현

def rotate(board, q):
    sx, sy, dx, dy = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1
    prev = board[sx][sy]
    rowLen = dx - sx + 1
    colLen = dy - sy + 1
    mini = prev

    for i in range(sy + 1, dy + 1, 1):
        prev, board[sx][i] = board[sx][i], prev
        mini = min(mini, prev)
    for i in range(sx + 1, dx + 1, 1):
        prev, board[i][dy] = board[i][dy], prev
        mini = min(mini, prev)
    for i in range(dy - 1, sy - 1, -1):
        prev, board[dx][i] = board[dx][i], prev
        mini = min(mini, prev)
    for i in range(dx - 1, sx - 1, -1):
        prev, board[i][sy] = board[i][sy], prev
        mini = min(mini, prev)

    return mini


def solution(rows, columns, queries):
    answer = []
    board = [[1 + i * columns + j for j in range(columns)] for i in range(rows)]
    for query in queries:
        answer.append(rotate(board, query))
    return answer