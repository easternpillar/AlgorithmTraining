# Problem:
# Given numbers from 0 to 9, return the number of prime numbers that can be made by permutations.

# My Solution:
import itertools


def solution(numbers):
    answer = 0
    strings = []

    for i in range(1, len(numbers) + 1):
        perm = list(itertools.permutations(numbers, i))
        strings.extend([*perm])

    strings = list(map(list, strings))
    for i in range(len(strings)):
        strings[i] = "".join(strings[i])
        strings[i] = int(strings[i])

    strings = sorted(list(set(strings)))

    for i in range(len(strings)):
        prime = 1
        if strings[i] <= 1:
            continue
        for div in range(2, strings[i], 1):
            if strings[i] % div == 0:
                prime = 0
                break
        if prime == 1:
            answer += 1

    return answer
