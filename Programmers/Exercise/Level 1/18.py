# Problem:
# Invert n natural number and return to an array with each digit as an element.

# My Solution:
def solution(n):
    answer = []

    while n != 0:
        n, r = divmod(n, 10)
        answer.append(r)
    return answer
