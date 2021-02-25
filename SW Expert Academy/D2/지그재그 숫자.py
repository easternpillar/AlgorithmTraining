# Problem:
# Print the result when you add odd numbers and subtract even numbers from numbers up to N.

# My Solution:
T = int(input())
for i in range(T):
    N = int(input())
    print("#{}".format(i + 1), end=" ")
    q, r = divmod(N, 2)
    if r > 0:
        print(q + 1)
    else:
        print(-q)
