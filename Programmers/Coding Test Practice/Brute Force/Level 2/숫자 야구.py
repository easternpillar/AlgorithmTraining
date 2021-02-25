# Problem:
# In number baseball game, return the number of possible cases.
# Condition(s):
# 1. The number is a triple digit and each number is between 1 and 9 with no redundancy.
# 2. Strike if the number has a number with same position.
# 3. Ball if the number has a number with different position.
# 4. Out if the number does not have a number.

# My Solution:
import itertools


def solution(baseball):
    answer = 0
    possible = list(itertools.permutations([x for x in range(1, 10)], 3))
    possible = list(map(list, possible))

    for i in range(len(baseball)):
        nums = str(baseball[i][0])
        strike = baseball[i][1]
        ball = baseball[i][2]
        rmv = []

        for j in range(len(possible)):
            n_strike = 0
            n_ball = 0
            tmp = "".join(list(map(str, possible[j])))
            print("nums:", nums, "compare:", tmp)
            for k in range(len(nums)):
                if nums[k] == tmp[k]:
                    n_strike += 1
                elif nums[k] in tmp:
                    n_ball += 1
                print("strike:", strike, n_strike, "ball:", ball, n_ball)

            if strike != n_strike or ball != n_ball:
                rmv.extend([j])
                print("remove:", j)

        rmv.sort(reverse=True)

        for remove in rmv:
            possible.pop(remove)

    answer = len(possible)
    return answer
