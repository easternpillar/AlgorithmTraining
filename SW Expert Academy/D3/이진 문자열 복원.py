# Problem:
#

# My Solution: DENIED.
# from itertools import product
#
#
# T = int(input())
#
# for i in range(T):
#     temp = list(map(int, input().split()))
#     length = sum(temp) + 1
#     prod=list(product(['0', '1'],repeat=length))
#     print("#{}".format(i + 1), end=" ")
#     flag = False
#
#     for p in globals()['prod']:
#         zz = 0
#         zo = 0
#         oz = 0
#         oo = 0
#         for j in range(0, len(p) - 1, 1):
#             if p[j] == '0':
#                 if p[j + 1] == '0':
#                     zz += 1
#                 else:
#                     zo += 1
#             else:
#                 if p[j + 1] == '0':
#                     oz += 1
#                 else:
#                     oo += 1
#
#         if temp == [zz, zo, oz, oo]:
#             flag = True
#             break
#
#     if not flag:
#         print("impossible")
#     else:
#         print("".join(p))

# My Solution: DENIED.
# from collections import deque
#
# T = int(input())
# for i in range(T):
#     temp = list(map(int, input().split()))
#     print("#{}".format(i + 1), end=" ")
#
#     q = deque([])
#     if temp[0] > 0 or temp[1] > 0:
#         q.append(['0', [0, 0, 0, 0]])
#     if temp[2] > 0 or temp[2] > 0:
#         q.append(['1', [0, 0, 0, 0]])
#
#     answer='impossible'
#     while q:
#         pop, use = q.popleft()
#         if use == temp:
#             answer=pop
#             break
#         if pop[-1] == '0':
#             if temp[0] - use[0] > 0:
#                 q.append([pop + '0', [use[0] + 1, use[1], use[2], use[3]]])
#             if temp[1] - use[1] > 0:
#                 q.append([pop + '1', [use[0], use[1] + 1, use[2], use[3]]])
#         else:
#             if temp[2] - use[2] > 0:
#                 q.append([pop + '0', [use[0], use[1], use[2] + 1, use[3]]])
#             if temp[3] - use[3] > 0:
#                 q.append([pop + '1', [use[0], use[1], use[2], use[3] + 1]])
#
#     print(answer)

for t in range(int(input())):
    a, b, c, d = map(int, input().split())

    if b == (c + 1):
        ans = '0' * (a + 1) + '1' * (d + 1) + '01' * c
    elif b == c and b != 0:
        ans = '0' * (a + 1) + '1' * (d + 1) + '01' * (c - 1) + '0'
    elif c == (b + 1):
        ans = '1' * (d + 1) + '0' * (a + 1) + '10' * b
    elif a * d == 0:
        if a:
            ans = '0' * (a + 1)
        else:
            ans = '1' * (d + 1)
    else:
        ans = 'impossible'

    print('#%d' % (t + 1), ans)
