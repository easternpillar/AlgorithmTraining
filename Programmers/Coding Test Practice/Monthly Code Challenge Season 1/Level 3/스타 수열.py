# Problem:
# Given a one-dimensional array of integers, return the length of the longest star sequence among all subsequences of this array.
# Condition(s):
# 1. A star sequence is an even numbered sequence with a length of 2 or more.
# 2. When the length of the star sequence is 2n, the number of elements in the intersection of the following n sets {x[0], x[1]}, {x[2], x[3]}, ..., {x[2n-2], x[2n-1]} is 1 or more with x[0] != x[1], x[2] != x[3], ..., x[2n-2] != x[2n-1].

# My Solution:
from collections import Counter


def solution(a):
    answer = -1
    count = Counter(a).most_common()

    for eli, num in count:

        if num < answer:
            continue

        idx = 0
        tmp_ans = 0
        while idx < len(a) - 1:
            if (a[idx] != eli and a[idx + 1] != eli) or a[idx] == a[idx + 1]:
                idx += 1
                continue

            tmp_ans += 1
            idx += 2

        answer = max(answer, tmp_ans)

    return answer * 2
