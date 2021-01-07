# Problem:
# Given a probability p to choose the right face on the first attempt and q to success if the right face is chosen, print whether the probability of success by flipping the face once is less than the probability of success by flipping twice.
# Condition(s):
# 1. If it fails to insert, turn the side over.

# My Solution:
TC = int(input())
for i in range(TC):
    p, q = map(float, input().split())
    print("#{}".format(i+1),end=" ")
    s1 = (1 - p) * q
    s2 = p * (1 - q) * q
    if s1 < s2:
        print("YES")
    else:
        print("NO")
