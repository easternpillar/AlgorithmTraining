# Problem:
# Given the number of alphabets, print every ten lines with a line break.

# My Solution:
T = int(input())
for i in range(T):
    N = int(input())
    print("#{}".format(i + 1))
    cnt = 0
    for j in range(N):
        alphabet, nums = input().split()
        for k in range(int(nums)):
            print(alphabet, end="")
            cnt += 1
            if cnt >= 10:
                print("")
                cnt = 0
    print("")
