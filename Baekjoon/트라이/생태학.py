# Problem:
# Reference: https://www.acmicpc.net/problem/4358

# My Solution:
import sys

tree_dict = dict()
tot = 0
while True:
    tree = sys.stdin.readline().rstrip()
    if tree:
        if tree in tree_dict:
            tree_dict[tree] += 1
        else:
            tree_dict[tree] = 1
        tot += 1
    else:
        break

answer = list(tree_dict.items())
answer.sort(key=lambda x: x[0])
for a in answer:
    print(a[0], end=" ")
    print('%.4f' % round(a[1] / tot*100, 4))
