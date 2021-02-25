# Problem:
# Given a string, print the remaining characters after matching the same two characters in alphabetical order.
# Condition(s):
# 1. Print "Good" if all characters are used for matching.

# My Solution:
from collections import Counter

T = int(input())
for i in range(T):
    string = list(input())
    answer = []

    cnt = Counter(string)

    for key in cnt:
        if cnt[key] % 2 == 1:
            answer.append(key)

    print("#{} {}".format(i + 1, "".join(sorted(answer)))) if answer else print("#{} Good".format(i + 1))
