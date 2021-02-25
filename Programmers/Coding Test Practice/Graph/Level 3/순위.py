# Problem:
# Given the results of matches, return the number of player whose rank can be set.

# My Solution:
def solution(n, results):
    answer = 0
    tt = [[[], []] for _ in range(n)]

    for i in range(len(results)):
        tt[results[i][0] - 1][0].append(results[i][1])
        tt[results[i][1] - 1][1].append(results[i][0])

    for i in range(n):

        for j in range(len(tt[i][0])):
            for k in range(len(tt[i][1])):
                if tt[tt[i][0][j] - 1][1].count(tt[i][1][k]) == 0:
                    tt[tt[i][0][j] - 1][1].append(tt[i][1][k])

        for j in range(len(tt[i][1])):
            for k in range(len(tt[i][0])):
                if tt[tt[i][1][j] - 1][0].count(tt[i][0][k]) == 0:
                    tt[tt[i][1][j] - 1][0].append(tt[i][0][k])

    for i in range(n):
        if len(tt[i][0]) + len(tt[i][1]) == n - 1:
            answer += 1
    return answer
