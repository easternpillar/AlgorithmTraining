# Problem:
# Given 2 string, return the jacquard similarity of multiple sets of two letters.
# Condition(s):
# 1. Multiply the similarity of jacquard by 65536 and discard below the decimal point.

# My Solution:
def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    s1 = []
    for i in range(len(str1) - 1):
        if 65 <= ord(str1[i]) <= 90 and 65 <= ord(str1[i + 1]) <= 90:
            s1.append(str1[i:i + 2])

    s2 = []
    for i in range(len(str2) - 1):
        if 65 <= ord(str2[i]) <= 90 and 65 <= ord(str2[i + 1]) <= 90:
            s2.append(str2[i:i + 2])

    tot = len(s1) + len(s2)
    if tot == 0:
        return 65536
    else:
        cnt = 0
        for i in range(len(s1)):
            idx = 0
            while idx < len(s2):
                if s1[i] == s2[idx]:
                    cnt += 1
                    s2.pop(idx)
                    break
                idx += 1
    answer = int((cnt / (tot - cnt)) * 65536)
    return answer
