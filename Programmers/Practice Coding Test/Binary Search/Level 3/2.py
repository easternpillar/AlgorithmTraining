# Problem:
# Given the number of persons who are waiting and times to be taken for reviewing immigration of each officer, return the minimum times to review the people.

# My Solution:
def solution(n, times):
    right = max(times) * n
    left = 1

    while left <= right:
        mid = (left + right) // 2
        tot = 0
        for time in times:
            tot += mid // time
            if tot >= n:
                break

        if tot >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
