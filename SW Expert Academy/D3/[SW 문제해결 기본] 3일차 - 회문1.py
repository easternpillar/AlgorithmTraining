# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14QpAaAAwCFAYi&categoryId=AV14QpAaAAwCFAYi&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9

# My Solution:
def palindrome(seq, length):
    tot = 0
    for j in range(0, len(seq) - length + 1, 1):
        if seq[j:j + length] == list(reversed(seq[j:j + length])):
            tot += 1
    return tot


answer = []
for i in range(10):
    length = int(input())
    board = []
    tot = 0

    for j in range(8):
        board.append(list(input()))

    for j in range(len(board)):
        tot += palindrome(board[j], length)

    board = list(map(list, zip(*board)))
    for j in range(len(board)):
        tot += palindrome(board[j], length)

    answer.append(tot)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
