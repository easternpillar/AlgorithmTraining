# Problem:
# Given an odd number, print the number of cases where the sum of the three primes is that odd number.

# My Solution: DENIED.
# def isPrime(num):
#     for i in range(2, int(num ** 0.5)+1, 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# T = int(input())
# for i in range(T):
#     N = int(input())
#     answer = 0
#     ans = []
#     print("#{}".format(i + 1), end=" ")
#
#     for j in range(2, N-3, 1):
#         if isPrime(j):
#             for k in range(j, N-3, 1):
#                 if isPrime(k):
#                     for l in range(k, N - 3, 1):
#                         if isPrime(l):
#                             # print(j,k,l)
#                             if j + k + l == N and {j, k, l} not in ans:
#                                 answer += 1
#                                 ans.append({j, k, l})
#
#     print(answer)

def is_prime_number(n):
    array = [True for _ in range(n + 1)]

    for i in range(2, int((n ** 0.5)) + 1):
        if array[i]:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [i for i in range(2, n + 1) if array[i]]


T = int(input())
p_list = is_prime_number(1000)
for i in range(T):
    N = int(input())
    print("#{}".format(i + 1), end=" ")

    answer = 0
    for j in range(len(p_list)):
        for k in range(j, len(p_list)):
            if N - p_list[j] - p_list[k] in p_list[k:]:
                answer += 1

    print(answer)
