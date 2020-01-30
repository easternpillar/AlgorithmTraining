# Problem:
# Given an arrangement of '(' and ')'; '()' means a laser and the rest of '(' and ')' means polls, return the number of divided polls.

# My Solution:
def solution(arrangement):
    answer = 0
    poll = 1
    length = len(arrangement)

    for i in range(0, length):
        cur = arrangement[i]
        if i == 0:
            continue
        prev = arrangement[i - 1]
        if cur == '(':
            poll = poll + 1
        if cur == ')':
            if prev == '(':
                poll = poll - 1
                answer = answer + poll
            else:
                poll = poll - 1
                answer = answer + 1
