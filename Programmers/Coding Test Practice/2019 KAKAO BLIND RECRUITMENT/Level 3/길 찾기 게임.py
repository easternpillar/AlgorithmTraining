# Problem:
# Given the coordination of binary tree nodes, return the pre-order and post-order sequence.
# Condition(s):
# 1. Every node has a different x value.
# 2. Nodes at the same level have the same y coordinate.
# 3. The y value of the child node is always less than the parent node.
# 4. The x value of all nodes in the left subtree is less than the x value of the node.
# 5. The x value of all nodes in the right subtree is greater than the x value of the node.


# My Solution:
import sys

sys.setrecursionlimit(10 ** 6)

preorder = list()
postorder = list()


def order(nodeList, levels, curLevel):
    n = nodeList[:]
    cur = n.pop(0)
    preorder.append(cur[0])
    if n:
        for i in range(len(n)):
            if n[i][1][1] == levels[curLevel + 1]:
                if n[i][1][0] < cur[1][0]:
                    order([x for x in nodeList if x[1][0] < cur[1][0]], levels, curLevel + 1)
                else:
                    order([x for x in nodeList if x[1][0] > cur[1][0]], levels, curLevel + 1)
    postorder.append(cur[0])


def solution(nodeinfo):
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)
    nodes = sorted(list(zip(range(1, len(nodeinfo) + 1), nodeinfo)), key=lambda x: (-x[1][1], x[1][0]))
    order(nodes, levels, 0)
    return [preorder, postorder]

