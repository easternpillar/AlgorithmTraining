# Problem:
# Print the number in ascending order.

# My Solution:
T = int(input())
for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    print("#{}".format(i + 1), end=" ")
    nums.sort()
    for num in nums:
        print(num, end=" ")
    print("")
