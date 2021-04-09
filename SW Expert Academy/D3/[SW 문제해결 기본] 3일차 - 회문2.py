# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9

# My Solution:
def palindrome(seq):
    for i in range(len(seq), 0, -1):
        for j in range(0, len(seq) - i + 1, 1):
            if seq[j:j + i] == list(reversed(seq[j:j + i])):
                return i


answer = []
for i in range(10):
    tn = int(input())
    board = []
    mLen = 1

    for j in range(100):
        board.append(list(input()))

    for j in range(len(board)):
        mLen = max(mLen, palindrome(board[j]))

    board = list(map(list, zip(*board)))
    for j in range(len(board)):
        mLen = max(mLen, palindrome(board[j]))

    answer.append(mLen)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
