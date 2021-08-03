# Problem:
# Reference: https://www.acmicpc.net/problem/20154

# My Solution:
import sys

letter = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
K = list(sys.stdin.readline().rstrip())
for i in range(len(K)):
    K[i] = letter[ord(K[i]) - ord('A')]

while True:
    temp = []
    for i in range(0, len(K), 2):
        if i + 1 < len(K):
            temp.append((K[i] + K[i + 1]) % 10)
        else:
            temp.append(K[i])
    K=temp
    if len(temp) == 1:
        if temp[0] % 2 == 0:
            print("You're the winner?")
            break
        else:
            print("I'm a winner!")
            break
