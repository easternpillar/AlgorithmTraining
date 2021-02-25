# Problem:
# Print out the rock, paper, scissors winner.
# Condition(s):
# 1. 1 is the scissors.
# 2. 2 is the rock.
# 3. 3 is the paper.

# My Solution:
A, B = map(int, input().split())
if A > B:
    if B == 1 and A == 3:
        print('B')
    else:
        print('A')
else:
    if A == 1 and B == 3:
        print('A')
    else:
        print('B')
