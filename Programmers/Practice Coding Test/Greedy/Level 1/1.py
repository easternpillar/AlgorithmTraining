# Problem:
# Given lists of students who lost their gym clothes and who have spare, return the number of students that can wear gym clothes.
# Condition(s):
# 1. If a student lost his/her gym clothes and has spare, the student wears it.

# My Solution:
def solution(n, lost, reserve):
    answer = 0
    answer = n - len(lost)
    solved = []
    for num in lost:
        if num in reserve:
            reserve.remove(num)
            solved.extend([num])
            answer += 1
    for num in lost:
        if num in solved:
            continue
        if num - 1 in reserve:
            reserve.remove(num - 1)
            answer += 1
        elif num + 1 in reserve:
            reserve.remove(num + 1)
            answer += 1

    return answer
