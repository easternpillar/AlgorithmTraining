# Problem:
# Given integers and the numbers of operations, return the maximum and minimum number that can be made.

# My Solution:
import itertools

n = int(input())
nums = list(map(int, input().split()))
nops = list(map(int, input().split()))
ops = [i for i in range(4) for j in range(nops[i])]

answer = set()
for tempop in list(itertools.permutations(ops)):
    fn = nums[0]
    for i in range(1, len(nums), 1):
        if tempop[i - 1] == 0:
            fn += nums[i]
        elif tempop[i - 1] == 1:
            fn -= nums[i]
        elif tempop[i - 1] == 2:
            fn *= nums[i]
        else:
            if fn < 0:
                fn = -(abs(fn) // nums[i])
            else:
                fn //= nums[i]
    answer.add(fn)

print(max(answer))
print(min(answer))
