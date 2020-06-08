# Problem:
# Given strings and a number 'n', return sorted list of strings that is sorted by index n.

# My Solution:
def solution(strings, n):
    answer = []
    strings.sort(key=lambda x: (x[n], x))
    answer = list(map(str, strings))
    return answer
