# Problem:
# Given a display order of gems, return the shortest section containing at least one of all gems.

# My Solution:
from collections import defaultdict


def solution(gems):
    result = [0, len(gems)]
    gem_kinds = len(set(gems))
    count_dict = defaultdict(int)
    count_dict[gems[0]] = 1

    left_idx, right_idx = 0, 0
    while right_idx < len(gems) and left_idx < len(gems):
        if len(count_dict) == gem_kinds:
            if result[1] - result[0] > right_idx - left_idx:
                result = [left_idx + 1, right_idx + 1]

            count_dict[gems[left_idx]] -= 1
            if count_dict[gems[left_idx]] == 0:
                del count_dict[gems[left_idx]]
            left_idx += 1

        else:
            right_idx += 1
            if right_idx == len(gems):
                break
            count_dict[gems[right_idx]] += 1

    return result
