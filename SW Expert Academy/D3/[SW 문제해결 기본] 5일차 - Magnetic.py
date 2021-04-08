# Problem:
# Reference: https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8

# My Solution:
def deadlock(seq):
    idx = 0
    total = 0
    flag = 0
    while idx < len(seq):
        if seq[idx] == '1':
            idx += 1
            while idx < len(seq):
                if seq[idx] == '1':
                    total += flag
                    flag = 0
                elif seq[idx] == '2':
                    flag = 1
                idx += 1
        if flag == 1:
            total += flag
        idx += 1
    return total


answer = []
for i in range(10):
    N = int(input())
    board = []
    for j in range(N):
        board.append(input().split())
    board = list(zip(*board))

    tot = 0
    for j in range(N):
        tot += deadlock(board[j])
    answer.append(tot)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
