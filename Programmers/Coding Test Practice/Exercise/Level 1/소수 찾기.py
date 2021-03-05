# Problem:
# Given the range of number, return the number of prime numbers.

# My Solution:
def solution(n):
    answer = 0
    isprime = [True for i in range(n)]
    for num in range(2, int(n ** 0.5) + 1):
        if isprime[num - 1]:
            for i in range(num + num, n + 1, num):
                isprime[i - 1] = False

    for b in isprime:
        if b:
            answer += 1
    return answer - 1

