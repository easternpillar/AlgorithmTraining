# Problem:
# Given the number of person and the number of

# My Solution:
import sys

answer = []
N, K = map(int, sys.stdin.readline().split())
person = [i for i in range(1, N + 1)]
idx = 0
while person:
    idx += K - 1
    idx = idx % len(person)
    answer.append(str(person.pop(idx)))

print('<' + ', '.join(answer) + '>')
