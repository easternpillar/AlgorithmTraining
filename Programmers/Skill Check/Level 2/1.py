# Problem:
# Given the number of players and sequence of a word chain game, return the number of player who are eliminated and the relay that the game is over.
# Condition(s):
# 1. A word can be used only once.
# 2. Return [0,0] if there is no wrong.

# My Solution:
def solution(n, words):
    answer = []
    used = [words[0]]

    for i in range(1, len(words)):
        if words[i] in used or words[i][0] != used[-1][-1]:
            return [i % n + 1, i // n + 1]
        else:
            used.append(words[i])

    return [0, 0]
