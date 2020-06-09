# Problem:
# Return a new integer ordered from large to small.

# My Solution:
def solution(n):
    answer = int("".join(sorted(str(n), reverse=True)))
    return answer
