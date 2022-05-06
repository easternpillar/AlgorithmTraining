# 링크: https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3
# 문제 접근
# 1. 연산자 단위 스플릿
# 2. 연산
from itertools import permutations


def solution(expression):
    oper = ['+', '-', '*']
    li = []
    temp = ''
    for i in range(len(expression)):
        if expression[i] == '-' or expression[i] == '+' or expression[i] == '*':
            li.append(temp)
            li.append(expression[i])
            temp = ''
            continue
        temp += expression[i]
    li.append(temp)

    maxi = 0
    temp = []
    for perm in permutations(oper, 3):
        copied = li[:]
        while len(copied) != 1:
            for op in perm:
                idx = 0
                while idx < len(copied):
                    if copied[idx] == op:
                        temp.pop()
                        temp.append(str(eval("".join(copied[idx - 1:idx + 2]))))
                        temp.extend(copied[idx + 2:])
                        copied = temp
                        temp = []
                        idx = 0
                        continue
                    temp.append(copied[idx])
                    idx += 1
                copied = temp
                temp = []
        maxi = max(maxi, abs(int(copied[0])))

    return maxi
