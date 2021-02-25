# Problem:
# Given a list of budget needed and the budget, return the maximum number of department that can be supported.

# My Solution:
def solution(d, budget):
    answer = 0
    d.sort()
    while answer != len(d):
        if budget >= d[answer]:
            budget -= d[answer]
            answer += 1
        else:
            break
    return answer
