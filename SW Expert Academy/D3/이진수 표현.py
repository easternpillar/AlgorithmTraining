# Problem:
# Given the integers N and M, print whether the last N bits of the binary representation of M are all 1.

# My Solution:
TC = int(input())
for i in range(TC):
    digit, num = map(int, input().split())
    mask = 0b1
    print("#{}".format(i + 1), end=" ")
    for j in range(1, digit):
        mask <<= 1
        mask += 1
    if mask & num == mask:
        print("ON")
    else:
        print("OFF")
