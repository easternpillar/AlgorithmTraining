# Problem:
# Reference: https://www.acmicpc.net/problem/5639

# My Solution:
import sys

sys.setrecursionlimit(10 ** 9)


def solution(start, end):
    if start > end:
        return

    div = end + 1

    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            div = i
            break

    solution(start + 1, div - 1)
    solution(div, end)
    print(tree[start])


tree = []
count = 0
while count <= 10000:

    try:
        temp = int(input())
    except:
        break
    tree.append(temp)
    count += 1

solution(0, len(tree) - 1)
