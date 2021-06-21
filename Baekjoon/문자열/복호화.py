# Problem:
# Reference: https://www.acmicpc.net/problem/9046

# My Solution:
import sys
from collections import Counter

for _ in range(int(sys.stdin.readline().rstrip())):
    string = sys.stdin.readline().rstrip()
    string = string.replace(' ', '')
    counter = Counter(string)
    temp = counter.most_common()

    if len(temp) > 1 and temp[0][1] == temp[1][1]:
        print('?')
    else:
        print(temp[0][0])
