# Problem:
# Given a sequence of alphabets, return the number of times that should be shifted.
# Condition(s):
# 1. One shift is needed for changing alphabet.
# 2. One shift is needed for moving to next element.

# My Solution:
def solution(name):
    answer = 0
    direction = 1
    i = 0
    complete = 0
    name = list(name)
    length = len(name)

    while True:

        temp = ord(name[i]) - ord('A')
        if temp <= 13:
            answer += temp
        else:
            answer += 26 - temp
        name[i] = 'A'
        complete += 1
        if name == ['A'] * length or complete == length:
            break

        max_a = [0, 0]

        idx = i
        while True:
            idx += 1
            if idx >= length:
                idx %= length
            if name[idx] != 'A':
                break
            else:
                max_a[0] += 1

        idx = i
        while True:
            idx -= 1
            if idx < 0:
                idx += length
            if name[idx] != 'A':
                break
            else:
                max_a[1] += 1

        if max_a[0] > max_a[1]:
            direction = -1
        else:
            direction = 1

        while name[i] == 'A':
            i += direction
            if i < 0:
                i += length
            if i >= length:
                i %= length
            answer += 1

    return answer

