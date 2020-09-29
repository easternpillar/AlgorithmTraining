# Problem:
# Given the number of buses, dispatch interval, and the boarding capacity, return the latest arrival time to get the bus.

# My Solution:
from collections import deque


def stringTotime(string):
    h, r = list(map(int, string.split(':')))
    return h, r


def timeTostring(h, t):
    string_h = ''
    string_t = ''
    if t < 0:
        h -= 1
        t = 59
        if h < 0:
            h = 23
    if h // 10 == 0:
        string_h = '0' + str(h)
    else:
        string_h = str(h)
    if t // 10 == 0:
        string_t = '0' + str(t)
    else:
        string_t = str(t)
    return string_h + ':' + string_t


def solution(n, t, m, timetable):
    sh = 9
    st = 0 - t
    tt = []
    for time in timetable:
        tt.append(stringTotime(time))
    tt.sort(key=lambda x: (x[0], x[1]))

    queue = deque(tt)

    for i in range(n):
        st += t
        q, r = divmod(st, 60)
        sh += q
        sh %= 24
        st = r
        sm = m

        while queue:
            if sm == 0:
                break
            th, tt = queue.popleft()

            if th < sh:
                sm -= 1

            elif th == sh and tt <= st:
                sm -= 1

            else:
                queue.appendleft([th, tt])
                break

    if sm != 0:
        answer = timeTostring(sh, st)
    else:
        answer = timeTostring(th, tt - 1)
    return answer
