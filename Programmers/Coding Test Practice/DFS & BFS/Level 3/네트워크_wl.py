# Problem:
# Given an array that has the information of connection between computers, return the number of networks.

# My Solution:
def solution(n, computers):
    answer = 0
    set_list = []
    net = [i for i in range(n)]

    for i in range(n - 1):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                flag = 0
                if not set_list:
                    set_list.extend([set([i, j])])
                    continue
                for k in range(len(set_list)):
                    if i in set_list[k] or j in set_list[k]:
                        set_list[k].add(i)
                        set_list[k].add(j)
                        flag = 1
                if flag == 0:
                    set_list.extend([set([i, j])])

    for i in range(len(set_list) - 1):
        for j in range(i + 1, len(set_list)):
            if set_list[i] & set_list[j]:
                set_list[i] = set_list[i] | set_list[j]
                set_list[j] = set()

    for i in range(len(set_list) - 1, -1, -1):
        if set_list[i] == set():
            set_list.pop(i)

    for num in range(n):
        for j in range(len(set_list)):
            if num in set_list[j] and num in net:
                net.remove(num)

    answer = len(set_list) + len(net)
    return answer

    print(set_list)
    for num in range(n):
        for j in range(len(set_list)):
            if num in set_list[j]:
                net.remove(num)
    print(len(set_list), len(net))
    answer = len(set_list) + len(net)
    return answer

    print(set_list)
    for num in range(n):
        for j in range(len(set_list)):
            if num in set_list[j]:
                net.remove(num)

    answer = len(set_list) + len(net)
    return answer


# Other Solution(s):
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            # for i in range(len(computers)-1, -1, -1):
            for i in range(0, len(computers)):
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)

    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1
    return answer

# Learned:
# 1. union(), intersection(): make union set and intersection set.