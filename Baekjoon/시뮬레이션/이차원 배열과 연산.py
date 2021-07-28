# Problem:
# Reference: https://www.acmicpc.net/problem/17140

# My Solution:
import sys
from collections import Counter

r, c, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
cnt = 0
while True:
    if cnt > 100:
        print(-1)
        break
    if len(arr) >= r and len(arr[0]) >= c:
        if arr[r-1][c-1] == k:
            print(cnt)
            break

    n_rows, n_cols = len(arr), len(arr[0])

    max_length = 0
    if n_rows >= n_cols:
        for i in range(len(arr)):
            counter = Counter(arr[i]).most_common()
            counter.sort(key=lambda x: (x[1], x[0]))
            temp = []
            for key, value in counter:
                if key == 0:
                    continue
                temp.extend([key, value])
            max_length = max(max_length, len(temp))
            arr[i] = temp[:]

        for a in arr:
            if len(a) < max_length:
                a.extend([0] * (max_length - len(a)))

    else:
        arr = list(map(list, list(zip(*arr))))
        for i in range(len(arr)):
            counter = Counter(arr[i]).most_common()
            counter.sort(key=lambda x: (x[1], x[0]))
            temp = []
            for key, value in counter:
                if key == 0:
                    continue
                temp.extend([key, value])
            max_length = max(max_length, len(temp))
            arr[i] = temp[:]

        for a in arr:
            if len(a) < max_length:
                a.extend([0] * (max_length - len(a)))
        arr = list(map(list, list(zip(*arr))))
    cnt += 1

