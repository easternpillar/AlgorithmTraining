# Problem:
# Given an example of a word chain game, return the player number and the number of rounds in which the person was eliminated.
# Condition(s):
# 1. The words that are already used cannot be used again.
# 2. A single letter word is not accepted.

# My Solution:
def solution(n, words):
    used = set()
    used.add(words[0])
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1] or len(words[i]) == 1 or words[i] in used:
            return [i % n + 1, i // n + 1]
        else:
            used.add(words[i])

    return [0, 0]
