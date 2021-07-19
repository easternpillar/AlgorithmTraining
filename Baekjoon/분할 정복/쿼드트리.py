# Problem:
# Reference: https://www.acmicpc.net/problem/1992

# My Solution:
import sys


def dc(b):
    global answer
    length = len(b)
    if length != 1:

        tot = 0
        for i in range(length):
            tot += sum(b[i])

        if tot == 0:
            answer += '0'

        elif tot == length ** 2:
            answer += '1'

        else:
            answer += '('

            b1 = []
            b2 = []
            b3 = []
            b4 = []
            for i in range(length // 2):
                b1.append(b[i][:length // 2])
                b2.append(b[i][length // 2:])
                b3.append(b[length // 2 + i][:length // 2])
                b4.append(b[length // 2 + i][length // 2:])

            dc(b1)
            dc(b2)
            dc(b3)
            dc(b4)
            answer += ')'
    else:
        answer += str(b[0][0])


N = int(sys.stdin.readline().rstrip())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
answer = ""

dc(board)
print(answer)
