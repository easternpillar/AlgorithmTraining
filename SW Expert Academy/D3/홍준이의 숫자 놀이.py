# Problem:
#

# My Solution:
def euclid(a, b):
    r0 = a
    r1 = b
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    temp = 0
    q = 0

    while r1 != 0:
        q = r0 // r1
        temp = r0
        r0 = r1
        r1 = temp - r1 * q
        temp = s0
        s0 = s1
        s1 = temp - s1 * q
        temp = t0
        t0 = t1
        t1 = temp - t1 * q

    return s0, t0


answer = []
for i in range(int(input())):
    A, B = map(int, input().split())
    answer.append(euclid(A, B))

for i in range(len(answer)):
    print("#{} {} {}".format(i + 1, answer[i][0], answer[i][1]))
