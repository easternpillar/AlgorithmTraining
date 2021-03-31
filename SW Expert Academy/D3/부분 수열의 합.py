# Problem:
# Given nature numbers, print the number of cases that the sum of more than one number equals the K.

# My Solution:
from itertools import combinations

answer = []
for i in range(int(input())):
    N, K = map(int, input().split())
    seq = list(map(int, input().split()))
    cnt = 0
    for j in range(1, len(seq) + 1):
        for comb in combinations(seq, j):
            if sum(comb) == K:
                cnt += 1

    answer.append(cnt)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
