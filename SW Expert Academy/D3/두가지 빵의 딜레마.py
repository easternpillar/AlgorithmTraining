# Problem:
# Given the prices of 2 breads and the balance, print the maximum number of breads that can be bought.

# My Solution:
T = int(input())
for i in range(T):
    A, B, C = map(int, input().split())
    print("#{} {}".format(i + 1), C // min(A, B))
