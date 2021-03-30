# Problem:
# Given two string lists, print the number of same strings.

# My Solution:
answer = []
for i in range(int(input())):
    N, M = map(int, input().split())
    li1 = set(input().split())
    li2 = set(input().split())
    s = li1.intersection(li2)
    answer.append(len(s))

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
