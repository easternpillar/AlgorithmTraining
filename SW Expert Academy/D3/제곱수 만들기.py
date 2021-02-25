# Problem:
# Given a natural number, print the smallest number that makes the result of multiplying a natural number by that number a power of a number.

# My Solution: DENIED.
# def prime_list(n):
#     era = [True for _ in range(n + 1)]
#     era[0] = False
#     era[1] = False
#     p_list = []
#     for i in range(2, n + 1):
#         if era[i]:
#             p_list.append(i)
#             for j in range(2, n // i + 1, 1):
#                 era[i * j] = False
#     return p_list
#
#
# def factorize(num):
#     answer = 1
#     for p in prime_list(num):
#         cnt = 0
#         while num % p == 0:
#             num = num // p
#             cnt += 1
#         if cnt % 2 == 1:
#             answer *= p
#         if num == 1:
#             break
#     return answer
#
#
# T = int(input())
# for i in range(T):
#     A = int(input())
#
#     print("#{} {}".format(i + 1, factorize(A)))

prime = [2]
for i in range(3, int(10000000 ** 0.5), 2):
    for p in prime:
        if not i % p: break
    else:
        prime.append(i)
answer = []

T = int(input())
for tc in range(T):
    A = int(input())
    res = 1

    for i in range(2, A + 1):
        if not A % i:
            cnt = 1
            A //= i
            while True:
                if not A % i:
                    cnt += 1
                    A //= i
                else:
                    break
            if cnt % 2:
                res *= i
            if A == 1:
                break
    print('#{} {}'.format(tc + 1, res))
