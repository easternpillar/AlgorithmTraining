# Reference: https://www.acmicpc.net/problem/14888
import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
oper_nums = list(map(int, sys.stdin.readline().split()))

answer = set()


def dfs(depth, tot, plus, minus, multiply, divide):
    if depth == N:
        answer.add(tot)
        return

    if plus > 0:
        dfs(depth + 1, tot + nums[depth], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(depth + 1, tot - nums[depth], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(depth + 1, tot * nums[depth], plus, minus, multiply - 1, divide)
    if divide > 0:
        dfs(depth + 1, -(abs(tot) // abs(nums[depth])) if tot < 0 or nums[depth] < 0 else tot // nums[depth], plus,
            minus, multiply, divide - 1)


dfs(1, nums[0], oper_nums[0], oper_nums[1], oper_nums[2], oper_nums[3])
print(max(answer))
print(min(answer))
