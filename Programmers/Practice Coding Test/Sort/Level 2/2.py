# Problem:
# Given a list of citations, return the H-Index.
# Condition(s):
# 1. Refer the Wiki about H-Index.

# My Solution:
def solution(citations):
    answer = 0
    length = len(citations)
    h = 0

    while True:
        citations.append(h)
        citations.sort()
        idx = citations.index(h)

        if len(citations[idx + 1:]) < h or len(citations[:idx]) > h:
            break
        answer = h
        citations.pop(idx)
        h += 1

    return answer
