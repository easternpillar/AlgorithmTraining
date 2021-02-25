# Problem:
# Given a board and the length of a word, print the number of space that the word can fit in.

# My Solution:
def horizontal(b, r, n, k):
    idx = 0
    total = 0
    while idx < n:
        if b[r][idx] == 1:
            cnt = 1
            while idx + 1 < n:
                idx += 1
                if b[r][idx] == 1:
                    cnt += 1
                else:
                    break
            if cnt == k:
                total += 1
        idx += 1
    return total


def vertical(b, c, n, k):
    idx = 0
    total = 0
    while idx < n:
        if b[idx][c] == 1:
            cnt = 1
            while idx + 1 < n:
                idx += 1
                if b[idx][c] == 1:
                    cnt += 1
                else:
                    break
            if cnt == k:
                total += 1
        idx += 1
    return total


T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    board = []
    print("#{}".format(i + 1), end=" ")
    answer = 0
    for _ in range(N):
        board.append(list(map(int, input().split())))

    for j in range(N):
        answer += horizontal(board, j, N, K)
        answer += vertical(board, j, N, K)

    print(answer)
