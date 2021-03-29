# Problem:
#

# My Solution:
def eratos(n):
    num = [True for _ in range(n + 1)]
    num[0] = False
    num[1] = False

    for i in range(2, n + 1):
        if num[i]:
            for j in range(i + i, n + 1, i):
                num[j] = False
    return num


answer = eratos(1000000)
for i in range(len(answer)):
    if answer[i]:
        print(i, end=" ")

# Other Solution:
answer = []
for n in range(2, 1000000):
    for j in range(2, int(n ** 0.5) + 1, 1):
        if n % j == 0:
            break
    else:
        answer.append(n)

for prime in answer:
    print(prime, end=' ')
