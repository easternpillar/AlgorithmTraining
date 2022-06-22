# Reference: https://www.acmicpc.net/problem/4358
import sys
from collections import Counter

li = []
while True:
    input_ = sys.stdin.readline().rstrip()
    if len(input_) > 30:
        continue
    if len(li) > 1000000:
        break
    if input_ == '':
        break
    li.append(input_)

length = len(li)
counter = list(Counter(li).items())
counter.sort(key=lambda x: (x[0], -x[1]))
for k, v in counter:
    print(k, format(round(v / length * 100, 4), '.4f'))
