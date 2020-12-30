# Problem:
# Given two times, print the sum of the two times.

# My Solution:
T = int(input())
for i in range(T):
    h1, m1, h2, m2 = map(int, input().split())
    print("#{} ".format(i + 1), end="")
    h = 0
    m = 0
    h = h1 + h2
    if h1 + h2 > 12:
        h -= 12
    m = m1 + m2
    if m >= 60:
        m -= 60
        h += 1
    print("{} {}".format(h, m))
