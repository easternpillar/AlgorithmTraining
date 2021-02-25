# Problem:
# Given the number of apartments and the range of the base stations, return how many more base stations should be installed so that all apartments receive radio waves.

# My Solution:
def solution(n, stations, w):
    answer = 0
    stations.append(n + w + 1)
    li = []
    cur = 0
    for s in stations:
        if s - w - cur > 0:
            li.append(s - w - cur - 1)
        cur = s + w
    print(li)
    for l in li:
        q, r = divmod(l, 2 * w + 1)
        if r == 0:
            answer += q
        else:
            answer += q + 1

    return answer
