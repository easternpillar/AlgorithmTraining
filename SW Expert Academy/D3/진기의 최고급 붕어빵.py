# Problem:
# Given the customer's arrival time and the time it takes to make K breads, print whether customers can pick up the bread right away.

# My Solution:
from collections import deque

answer = []

for i in range(int(input())):
    N, M, K = map(int, input().split())
    arrival = sorted(list((map(int, input().split()))))
    q = deque(arrival)
    bread = 0
    time = 0
    idx = 0
    out = ''
    flag = True
    if arrival[0] == 0:
        answer.append('Impossible')
        continue
    while time <= arrival[-1]:
        time += 1
        if time % M == 0:
            bread += K
        while arrival[idx] == time:
            if bread <= 0:
                out = 'Impossible'
                flag = False
                break
            else:
                bread -= 1
                idx += 1
                if idx >= len(arrival):
                    out = 'Possible'
                    flag = False
                    break
        if not flag:
            break
    answer.append(out)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
