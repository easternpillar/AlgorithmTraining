# Problem:
# Given integers and the numbers of operations, return the maximum and minimum number that can be made.

# My Solution:
import itertools

n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))

op = ''
for idx, oper in enumerate(opers):
    op += str(idx) * oper

op = list(map(int, op))
res_list = []
for now_op in set(itertools.permutations(op, len(op))):
    res = nums[0]
    for idx in range(n - 1):
        if now_op[idx] == 0:
            res += nums[idx + 1]
        elif now_op[idx] == 1:
            res -= nums[idx + 1]
        elif now_op[idx] == 2:
            res *= nums[idx + 1]
        elif now_op[idx] == 3:
            res = res // nums[idx + 1] if res > 0 else ((res * -1) // nums[idx + 1]) * -1
    res_list.append(res)

print(max(res_list))
print(min(res_list))
