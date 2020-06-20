# Problem:
# Given a begin word, a target word, and a list of words, return the minimum number of change that makes begin word to target word.
# Condition(s):
# 1. Only one character can be changed at once.
# 2. Word can be changed only if it is in words list.

# My Solution:
def solution(begin, target, words):
    used = [set() for i in range(len(words))]
    words = list(map(list, zip(words, [0 for i in range(len(words))], used)))
    stack = [[begin, 0, set()]]
    d_list = []

    while stack:
        word = stack.pop()
        depth = word[1]

        if word[0] == target:
            d_list.append(word[1])
            continue

        for i in range(len(words)):
            if word[0] == words[i][0] or words[i][0] in word[2]:
                continue
            same = 0
            diff = 0
            for j in range(len(word[0])):
                if word[0][j] == words[i][0][j]:
                    same += 1
                else:
                    diff += 1
            if same == len(word[0]) - 1 and diff == 1:
                temp = words[i].copy()
                temp[1] = depth + 1
                temp[2].add(word[0])
                temp[2] = words[i][2] | word[2]
                stack.append(temp)

    if d_list:
        answer = min(d_list)
    else:
        answer = 0

    return answer
