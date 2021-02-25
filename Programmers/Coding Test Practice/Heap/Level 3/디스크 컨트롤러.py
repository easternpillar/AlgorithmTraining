# Problem:
# Given jobs for the disk with starting time and time that will be taken, return average time of jobs to be completed.
# Condition(s):
# 1. If disk does not have any works, the job that comes first should be taken.

# My Solution:
import heapq


def solution(jobs):
    answer = 0
    h = []
    length = len(jobs)
    idx = 0
    time = 0
    jobs.sort()

    while idx < length:
        if not h:
            heapq.heappush(h, (jobs[idx][1], jobs[idx]))
            time = jobs[idx][0]
            idx += 1

            while idx < length:
                if jobs[idx][0] == time:
                    heapq.heappush(h, (jobs[idx][1], jobs[idx]))
                    idx += 1
                else:
                    break

        while h:
            cur = heapq.heappop(h)

            answer += (time - cur[1][0]) + cur[1][1]
            time += cur[1][1]

            while idx < length:
                if jobs[idx][0] < time:
                    heapq.heappush(h, (jobs[idx][1], jobs[idx]))
                    idx += 1
                else:
                    break

    answer = int(answer / length)
    return answer
