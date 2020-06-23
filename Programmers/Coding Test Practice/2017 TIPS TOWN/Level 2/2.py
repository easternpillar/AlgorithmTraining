# Problem:
# Given the number of participants and the player numbers in the tournament, return the rounds to meet.

# My Solution:
def solution(n, a, b):
    answer = 0
    if a > b:
        a, b = b, a
    a -= 1
    b -= 1
    if a % 2 == 0 and b == a + 1:
        return answer + 1
    while True:
        a, b = a // 2, b // 2
        print(a, b)
        answer += 1
        if a % 2 == 0 and b == a + 1:
            return answer + 1
