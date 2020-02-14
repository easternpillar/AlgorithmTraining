# Problem:
# Given a list of strings,return the maximum and minimum value.
# Condition(s):
# 1. I: insert an integer.
# 2. D 1: delete maximum integer.
# 3. D -1: delete minimum integer.
# 4. if it is empty, return [0, 0], or return [maximum, minimum].

# My Solution: DENIED.
# import heapq
#
#
# def solution(operations):
#     answer = []
#     h = []
#
#     for operation in operations:
#         temp = operation.split()
#         if temp[0] == 'I':
#             heapq.heappush(h, int(temp[1]))
#         elif temp[0] == 'D':
#             if h:
#                 if temp[1] == '-1':
#                     heapq.heappop(h)
#                 elif temp[1] == '1':
#                     h.pop()
#
#     if h:
#         answer = [h[-1], h[0]]
#     else:
#         answer = [0, 0]
#     return answer


def solution(operation):
    answer = []
    temp = []
    for oper in operation:
        if oper.split()[0] == 'I':
            temp.append(int(oper.split()[1]))
        elif oper.split()[0] == 'D':
            if len(temp) != 0:
                if oper.split()[1] == '1':
                    temp.remove(max(temp))
                elif oper.split()[1] == '-1':
                    temp.remove(min(temp))

    if len(temp) == 0:
        answer = [0, 0]
    else:
        answer = [max(temp), min(temp)]

    return answer
