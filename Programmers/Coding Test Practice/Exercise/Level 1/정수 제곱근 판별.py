# Problem:
# If the square of positive integer x, return the square of x+1, and if n is not the square of positive integer x, return the square of -1.

# My Solution:
def solution(n):
    answer = 0
    if n ** 0.5 == int(n ** 0.5):
        answer = (n ** 0.5 + 1) ** 2
    else:
        answer = -1
    return answer
