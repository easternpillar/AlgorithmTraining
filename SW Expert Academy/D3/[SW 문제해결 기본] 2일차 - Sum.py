# Problem:
# Given a 2-dimension array filled with integers, print the maximum of the horizontal sum, vertical sum, and diagonal sum.

# My Solution:
answer = []
for i in range(10):
    tn = int(input())
    board = []
    mVal = 0
    for j in range(100):
        board.append(list(map(int, input().split())))
        mVal = max(sum(board[j]), mVal)

    board = list(map(list, list(zip(*board))))
    for j in range(100):
        mVal = max(sum(board[j]), mVal)

    tot1 = 0
    tot2 = 0
    for j in range(100):
        tot1 += board[j][j]
        tot2 += board[99 - j][j]
        mVal = max(mVal, max(tot1, tot2))

    answer.append(mVal)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
