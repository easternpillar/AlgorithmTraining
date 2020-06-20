# Problem:
# Given flight tickets that have departure and arrival, return the route that all tickets are used.
# Condition(s):
# 1. If there are more than one possible path, return the path in alphabetical order.

# My Solution:
def solution(tickets):
    answer = ["ICN"]
    stack = [["ICN", []]]

    while stack:
        temp = stack.pop()

        tmp_list = []
        for i in range(len(tickets)):
            used = temp[1].copy()
            if i in used:
                continue

            if tickets[i][0] == temp[0]:
                used.append(i)
                tmp_list.append([tickets[i][1], used])

                if len(used) == len(tickets):
                    for idx in used:
                        answer.append(tickets[idx][1])
                    return answer

        stack.extend(sorted(tmp_list, reverse=True))
