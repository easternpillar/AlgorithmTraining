# Problem:
# Given N positive integers, print the monotonically increasing maximum of the product of two positive integers.

# My Solution:
def danzo(num):
    num = str(num)
    for i in range(len(num) - 1):
        if int(num[i]) > int(num[i + 1]):
            return False
    return True


T = int(input())
for i in range(T):
    print("#{}".format(i + 1), end=" ")
    N = int(input())
    li = list(map(int, input().split()))
    ans = []
    maxi = -1

    for j in range(N - 1):
        for k in range(j + 1, N, 1):
            tmp = li[j] * li[k]
            if danzo(tmp) and tmp > maxi:
                maxi = tmp

    print(maxi)
