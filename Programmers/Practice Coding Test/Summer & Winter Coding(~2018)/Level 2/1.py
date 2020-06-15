# Problem:
# Given the preceding skill sequence and example skill trees, return the number of possible skill trees.

# My Solution:
def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        avail = [False for i in range(len(skill))]
        avail[0] = True

        for s in tree:
            if s in skill:
                if avail[skill.index(s)]:
                    if skill.index(s) + 1 < len(skill):
                        avail[skill.index(s) + 1] = True
                else:
                    answer += 1
                    break

    answer = len(skill_trees) - answer
    return answer
