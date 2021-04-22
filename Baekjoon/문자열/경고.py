# Problem:
# Given the current time and the explosion time, print the hiding time.
# Condition(s):
# 1. Hide for at least 1 second.

# My Solution:
import sys

ch, cm, cs = list(map(int, sys.stdin.readline().split(':')))
bh, bm, bs = list(map(int, sys.stdin.readline().split(':')))

if ch == bh and cm == bm and cs == bs:
    print("24:00:00")
else:
    if ch > bh:
        bh += 24

    bh -= ch
    bm -= cm
    if bm < 0:
        bh -= 1
        bm += 60
    bs -= cs
    if bs < 0:
        bm -= 1
        bs += 60
        if bm < 0:
            bm += 60
            bh -= 1

    print("{}:{}:{}".format(str(bh).rjust(2, '0'), str(bm).rjust(2, '0'), str(bs).rjust(2, '0')))
