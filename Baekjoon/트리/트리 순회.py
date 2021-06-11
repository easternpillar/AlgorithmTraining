# Problem:
# Reference: https://www.acmicpc.net/problem/1991

# My Solution:
import sys
from collections import defaultdict


def preorder(start):
    print(start, end="")
    if nodes[start][0] != '.':
        preorder(nodes[start][0])
    if nodes[start][1] != '.':
        preorder(nodes[start][1])


def postorder(start):
    if nodes[start][0] != '.':
        postorder(nodes[start][0])
    if nodes[start][1] != '.':
        postorder(nodes[start][1])
    print(start, end="")


def inorder(start):
    if nodes[start][0] != '.':
        inorder(nodes[start][0])
    print(start, end="")
    if nodes[start][1] != '.':
        inorder(nodes[start][1])


N = int(sys.stdin.readline().rstrip())
nodes = defaultdict(list)

for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    nodes[node].extend([left, right])

preorder('A')
print()
inorder('A')
print()
postorder('A')
