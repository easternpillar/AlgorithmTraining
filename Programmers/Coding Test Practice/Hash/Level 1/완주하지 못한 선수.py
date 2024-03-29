# Problem:
# Given two lists of names: participant and completion, find the person who did not complete the race.
# Condition(s):
# 1. Only one person did not complete the race.

# My Solution: DENIED. (Time complexity is not satisfied.)
# def solution(participant, completion):
#     for name in participant:
#             if participant.count(name)!=completion.count(name):
#                 return name

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# Other Solution(s):
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

