# Problem:
# Given the monthly water usage, print out the water bill for the lower of the two water companies.
# Condition(s):
# 1. P won per liter must be paid to Company A.
# 2. Q won for basic charge and S won for each excess liter if the usage exceeds R must be paid to Company B.

# My Solution:
T = int(input())
for i in range(T):
    P, Q, R, S, W = map(int, input().split())
    print("#{}".format(i + 1), end=" ")
    A = W * P
    B = Q
    if W > R:
        B += (W - R) * S

    print(A if A < B else B)
