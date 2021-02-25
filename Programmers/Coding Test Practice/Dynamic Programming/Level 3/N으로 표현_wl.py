# Problem:
# Given a number to use and another number to make, return the minimum number of use.
# Condition(s):
# 1. Return -1 if the minimum number is greater than 8.
# 2. Ignore the remainder in division.

# My Solution:
def solution(N, number):
    answer = 0
    s = [set() for _ in range(8)]
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1

    return answer

# Learned:
# 1. enumerate(): use if you want to know how many times of loop.
# 2. Dynamic Programming: uses the smaller solutions to solve the bigger problems.
