# Problem:
# Given a number, return maximum number when k numbers are removed.

# My Solution: Denied.
# def solution(number, k):
#     answer = []
#     number = list(number)
#     len_num = len(number)
#     idx = 0
#     done = len_num - k
#
#     while len(answer) < done:
#         maximum = max(number[idx:k + 1])
#         answer.append(maximum)
#         idx += number[idx:].index(maximum) + 1
#         k += 1
#
#         if done - len(answer) == len(number[idx:]):
#             answer.extend(number[idx:])
#             break
#
#     return "".join(answer)

def solution(number, k):
    collected = []

    for (i, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        if k == 0:
            collected += number[i:]
            break

        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer

# Learned:
# 1. Stack: stack is better because number[idx:] has O(n) time complexity.