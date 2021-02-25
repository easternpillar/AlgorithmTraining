# Problem:
# Given a table of a database, return the number of candidate keys.

# My Solution:
import itertools


def solution(relation):
    num = 1
    cols = [i for i in range(len(relation[0]))]

    used = set()
    while True:
        ts = set()
        if len(cols) < num:
            break
        for temp in (list(itertools.combinations(cols, num))):

            flag = 1
            if used:
                for use in used:
                    s1 = set(use)
                    s2 = set(temp)
                    if len(s1.intersection(s2)) == len(s1):
                        flag = 0

            if flag == 0:
                continue

            s = set()
            for i in range(len(relation)):
                string = ""
                for t in temp:
                    string += relation[i][t]
                s.add(string)

                if len(relation) == len(s):
                    ts.add(temp)

        used = used.union(ts)

        num += 1
    return len(used)
