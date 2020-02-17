# Problem:
# Given patterns how 3 students choose the answer and the answer, return which student will be taken the most score.
# Condition(s):
# 1. If there are more than one students that take the most score, return with ascending order of indices.

# My Solution:
def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            cnt[0] += 1
        if answers[i] == p2[i % len(p2)]:
            cnt[1] += 1
        if answers[i] == p3[i % len(p3)]:
            cnt[2] += 1

    zipped = list(zip(cnt, [1, 2, 3]))
    zipped.sort(reverse=True)

    maximum = 0

    for i in range(len(zipped)):
        if zipped[i][0] >= maximum:
            answer.extend([zipped[i][1]])
            maximum = zipped[i][0]
        else:
            break

    answer.sort()

    return answer
