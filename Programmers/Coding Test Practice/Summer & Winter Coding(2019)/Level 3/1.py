# Problem:
# Given the number of folds, return 0 if the fold is v-shaped, 1 if it is ^-shaped.

# My Solution:
def solution(n):
    answer = [0]
    i = 0
    while i < n - 1:
        prev = answer[:]
        answer.append(0)
        for p in list(reversed(prev)):
            if p == 0:
                answer.append(1)
            else:
                answer.append(0)
        i += 1
    return answer
