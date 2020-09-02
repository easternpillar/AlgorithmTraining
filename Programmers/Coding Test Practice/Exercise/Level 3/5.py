# Problem:
# Given the time remaining until work and the amount of work for each job, return a value that minimizes overtime fatigue.
# Condition(s):
# 1. 1 workload can be handled in 1 hour.
# 2. Overtime fatigue is the sum of the squares of each workload.

# My Solution:
def solution(n, works):
    answer = 0
    works.append(0)
    works.sort(reverse=True)
    idx = 0
    smooth_idx = 0

    while n > 0:
        if smooth_idx < len(works) - 1:
            while works[smooth_idx] > works[smooth_idx + 1]:
                for i in range(smooth_idx + 1):
                    if works[i] - 1 < 0:
                        if sum(works) == 0:
                            return 0
                        continue
                    works[i] -= 1
                    n -= 1
                    if n == 0:
                        for i in range(len(works)):
                            answer += works[i] * works[i]
                        return answer
        if smooth_idx == len(works) - 1:
            idx += 1
            if works[i] - 1 < 0:
                if sum(works) == 0:
                    return 0
                continue
            works[idx % len(works)] -= 1
            n -= 1

        smooth_idx += 1
    for i in range(len(works)):
        answer += works[i] * works[i]
    return answer
