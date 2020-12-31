# Problem:
# Given a number, Given a number that is the product of 2,3,5,7,11, print the squared number of each factor.

# My Solution:
T = int(input())
nums = [2, 3, 5, 7, 11]
for i in range(T):
    N = int(input())
    print("#{}".format(i + 1), end=" ")

    for num in nums:
        temp = N
        cnt = 0
        while True:
            q, r = divmod(temp, num)
            if r > 0:
                print(cnt, end=" ")
                break
            else:
                cnt += 1
                temp = q
    print("")
