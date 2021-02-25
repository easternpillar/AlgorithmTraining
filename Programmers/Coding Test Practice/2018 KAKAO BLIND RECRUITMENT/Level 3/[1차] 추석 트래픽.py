# Problem:
# Given a list of log data, return the maximum number of requests processed in 1 second (=1,000 milliseconds).

# My Solution:
def solution(lines):
    li = []
    for log in lines:
        temp = log.split(" ")
        ptime = float(temp[2][:-1])
        hms = list(map(float, temp[1].split(":")))
        etime = round(24 * 3600 + hms[0] * 3600 + hms[1] * 60 + hms[2], 4)
        stime = round(etime - ptime + 0.001, 4)
        li.append([stime, etime])

    mval = 1
    for i in range(len(li) - 1):
        etime = li[i][1]

        cnt = 1
        for j in range(i + 1, len(li)):

            if li[j][0] - 1 < etime:
                cnt += 1

        if cnt > mval:
            mval = cnt
    answer = mval
    return answer
