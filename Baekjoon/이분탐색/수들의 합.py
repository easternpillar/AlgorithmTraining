# Problem:
# Given a natural number, print the maximum numbers of natural numbers to make the number by sum.

# My Solution:
import sys

S = int(sys.stdin.readline().rstrip())
tot = 0
add = 1
while tot <= S:
    tot += add
    add += 1
print(add - 2)

# Other Solution:
# import sys
#
# S = int(sys.stdin.readline().rstrip())
#
# start = 1
# end = S
# answer = 0
#
# while start <= end:
#     mid = (start + end) // 2
#     if mid * (mid + 1) // 2 <= S:
#         answer = mid
#         start = mid + 1
#     else:
#         end = mid - 1
#
# print(answer)
