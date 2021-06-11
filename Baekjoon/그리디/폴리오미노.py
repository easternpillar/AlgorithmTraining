# Problem:
# Reference: https://www.acmicpc.net/problem/1343

# My Solution:
import sys

board = sys.stdin.readline().rstrip()
splitted = board.split('.')

answer = ''
flag = True
for s in splitted:
    if len(s) % 2 != 0:
        print(-1)
        flag = False
        break
    else:
        if len(s) % 4 == 0:
            answer += 'AAAA' * (len(s) // 4)
        else:
            answer += 'AAAA' * (len(s) // 4)
            answer += 'BB'
        answer += '.'

if flag:
    print(answer[:-1])
