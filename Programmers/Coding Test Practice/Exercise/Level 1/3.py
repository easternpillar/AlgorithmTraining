# Problem:
# Given a list of integers, return a list that the same number does not com out in a row.

# My Solution:
def solution(arr):
    pre = -1
    answer = []
    for num in arr:
        if pre == num:
            continue
        else:
            pre = num
            answer.append(num)

    return answer
