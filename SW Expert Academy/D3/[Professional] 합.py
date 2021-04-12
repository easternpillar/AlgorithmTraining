# Problem:
# Given a integer list, print the maximum sum of sequence.

# My Solution:
answer = []
for i in range(int(input())):
    N = int(input())
    integers = list(map(int, input().split()))
    left = 0
    right = 1
    tot = 0
    maximum = max(integers)
    while left < right <= len(integers):
        tot += integers[right - 1]
        if tot >= 0:
            maximum = max(maximum, tot)
            right += 1
        else:
            tot = 0
            left = right
            right = left + 1
    answer.append(maximum)

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
