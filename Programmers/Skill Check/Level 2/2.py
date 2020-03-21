# Problem:
# Given wieghts of people and limit weight of boat, return how many boats will be needed.
# Condition(s):
# 1. The limit of passengers is 2 people.

def solution(people, limit):
    answer = 0
    people.sort()
    front = 0
    back = len(people) - 1

    while front <= back:
        if people[front] + people[back] <= limit:
            front += 1
            back -= 1
        else:
            back -= 1
        answer += 1

    return answer
