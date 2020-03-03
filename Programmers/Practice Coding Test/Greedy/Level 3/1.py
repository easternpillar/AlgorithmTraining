# Problem:
# Given costs of brdige constructions among islands, return the minimum costs of brdiges satisfying that all islands are connected.
# Condition(s):
# There is only one bridge among two islands at most.

# My Solution:
def solution(n, costs):
    answer = 0
    costs.sort(reverse=True, key=lambda x: x[2])
    connected = []
    notyet = []

    temp = costs.pop()
    connected.extend([temp[0], temp[1]])
    answer += temp[2]

    while costs:
        temp = costs.pop()

        if temp[0] in connected and temp[1] in connected:
            continue

        if temp[0] in connected or temp[1] in connected:
            connected.extend([temp[0], temp[1]])
            connected = list(set(connected))
            answer += temp[2]
        else:
            notyet.extend([temp])
            notyet.sort(reverse=True, key=lambda x: x[2])

        if notyet:
            idx = len(notyet) - 1

            while True:
                if idx < 0:
                    break

                if notyet[idx][0] in connected or notyet[idx][1] in connected:
                    popped = notyet.pop(idx)
                    connected.extend([popped[0], popped[1]])
                    connected = list(set(connected))
                    idx = len(notyet) - 1
                    answer += popped[2]
                    continue
                else:
                    idx -= 1

        if len(connected) == n:
            break

    return answer
