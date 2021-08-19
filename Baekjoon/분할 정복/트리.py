# Problem:
# Reference: https://www.acmicpc.net/problem/4256

# My Solution:
import sys
from collections import defaultdict


def postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        print(preorder[0], end=" ")
        return
    if len(preorder) == 2:
        print(preorder[1], preorder[0], end=" ")
        return

    root = preorder[0]
    root_idx = inorder.index(root)
    left_tree = inorder[:root_idx]
    right_tree = inorder[root_idx + 1:]
    postorder(preorder[1:1 + len(left_tree)], left_tree)
    postorder(preorder[1 + len(left_tree):], right_tree)
    print(preorder[0], end=" ")


for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    nodes = defaultdict(list)
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    postorder(preorder, inorder)
    print()
