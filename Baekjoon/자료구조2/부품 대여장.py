# Problem:
# Reference: https://www.acmicpc.net/problem/21942

# My Solution:
import sys
from collections import defaultdict
import datetime


def calculate(dt1, dt2):
    dt1 = datetime.datetime.strptime(dt1, "%Y-%m-%d %H:%M")
    dt2 = datetime.datetime.strptime(dt2, "%Y-%m-%d %H:%M")
    sub = (dt2 - dt1).total_seconds() // 60
    if sub > dead:
        return sub - dead
    else:
        return 0


N, L, F = sys.stdin.readline().split()
N = int(N)
F = int(F)
pd, phm = L.split('/')
ph, pm = phm.split(':')
dead = int(pd) * 24 * 60 + int(ph) * 60 + int(pm)
rent = defaultdict(str)
rented = defaultdict(bool)
penalty = defaultdict(int)
for _ in range(N):
    date, time, part, name = sys.stdin.readline().split()
    if rented[(part, name)]:
        penalty[name] += calculate(rent[(part, name)], date + ' ' + time) * F
        rented[(part, name)] = False
    else:
        rented[(part, name)] = True
        rent[(part, name)] = date + ' ' + time

flag = False
for n, p in sorted(tuple(penalty.items()), key=lambda x: x[0]):
    if p > 0:
        flag = True
        print(n, int(p))
if not flag:
    print(-1)
