# Problem:
# Given a string consisting of letters S, D, T, *, and #, return the total score.
# Condition(s):
# 1. S, D, T means 1, 2, 3 squares.
# 2. * makes the corresponding score and the score just before double each.
# 3. # makes the corresponding score negative.

# My Solution:
def solution(dartResult):
    answer = 0
    start = 0
    idx = 0
    li = []
    while start < len(dartResult):
        idx += 1
        if dartResult[idx] == 'S' or dartResult[idx] == 'D' or dartResult[idx] == 'T':
            if dartResult[idx] == 'S':
                li.append(int(dartResult[start:idx]))
            elif dartResult[idx] == 'D':
                li.append(int(dartResult[start:idx]) ** 2)
            else:
                li.append(int(dartResult[start:idx]) ** 3)
            start = idx + 1
        elif dartResult[idx] == '*' or dartResult[idx] == '#':
            li.append(dartResult[idx])
            start = idx + 1

    print(li)
    for i in range(len(li)):
        if li[i] == '*':
            cnt = 0
            for j in range(i, -1, -1):
                if cnt == 2:
                    break
                if li[j] == '*' or li[j] == '#':
                    continue
                li[j] *= 2
                cnt += 1
        elif li[i] == '#':
            for j in range(i, -1, -1):
                if li[j] == '*' or li[j] == '#':
                    continue
                li[j] *= -1
                break

    for temp in li:
        if temp == '*' or temp == '#':
            continue
        answer += temp
    return answer
