# Problem:
# Given a list of numbers, return the number of prime numbers made by sum of 3 numbers.

# My Solution:
def solution(nums):
    answer = 0
    prime = [True for i in range(10000)]
    for i in range(len(prime) - 1):
        for j in range(i + 1, len(prime)):
            if (j + 2) % (i + 2) == 0:
                prime[j] = False

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                tot = nums[i] + nums[j] + nums[k]
                if prime[tot - 2]:
                    answer += 1

    return answer
