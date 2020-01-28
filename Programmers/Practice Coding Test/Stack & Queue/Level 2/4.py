# Problem:
# Given the priorities of documents to be printed and the location of document to check, return the number of times the document will been printed.
# Condition(s):
# 1. The document will be relocated to the end of sequence if there is any document that has higher priority.

# My Solution:
def solution(priorities, location):
    printed = []

    i = 0
    cnt = 1
    while True:
        if i == len(priorities):
            i = i - len(priorities)
        if i in printed or priorities[i] != max(priorities):
            i = i + 1
            continue
        if priorities[i] != max(priorities):
            printed.extend([i])
            i = i + 1
        else:
            if i == location:
                return cnt
            priorities[i] = 0
            cnt = cnt + 1
