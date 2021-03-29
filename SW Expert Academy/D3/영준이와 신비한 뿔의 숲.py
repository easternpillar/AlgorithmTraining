# Problem:
# Given the number of horns and animals, print the number of unicorns and twinhorns.

# My Solution:
uni = []
twin = []
for i in range(int(input())):
    n, m = map(int, input().split())
    for j in range(m + 1):
        if j + (m - j) * 2 == n:
            uni.append(j)
            twin.append(m - j)
            break

for i in range(len(uni)):
    print("#{} {} {}".format(i + 1, uni[i], twin[i]))
