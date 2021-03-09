# Problem:
# Print the number of prime numbers containing a specific number between the given range of numbers.

# My Solution:
prime = [True] * ((10 ** 6) + 1)
prime[0] = prime[1] = False
for i in range(2, len(prime)):
    if prime[i]:
        for j in range(2 * i, len(prime), i):
            prime[j] = False

T = int(input())
for i in range(T):
    D, A, B = map(int, input().split())
    cnt = 0
    for j in range(A, B + 1):
        if str(D) in str(j) and prime[j]:
            cnt += 1

    print("#{} {}".format(i + 1, cnt))
