# Problem:
# Given a number of stages and a list of stages that users are staying, return failure rate by descending order.

# My Solution:
def solution(N, stages):
    answer = []
    stages.sort()
    length = len(stages)
    fail = [0 for i in range(N)]
    for i in range(1, N + 1):
        if stages.count(i) == 0:
            continue
        fail[i - 1] = stages.count(i) / length
        length -= stages.count(i)
    rank = list(zip([i for i in range(1, N + 1)], fail))
    rank.sort(key=lambda x: x[1], reverse=True)
    for stage in rank:
        answer.append(stage[0])
    return answer
