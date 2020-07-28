# Problem:
# Given a MxM key and a NxN lock, return whether the key can open the lock.

# My Solution:
import copy


def solution(key, lock):
    flag = 1
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if lock[i][j] == 0:
                flag = 0
                break
        if flag == 0:
            break
    if flag == 1:
        return True

    keylen = len(key)
    locklen = len(lock)
    new = [[0 for i in range(locklen + 2 * (keylen - 1))] for j in range(locklen + 2 * (keylen - 1))]

    for i in range(keylen - 1, keylen + locklen - 1):
        for j in range(keylen - 1, keylen + locklen - 1):
            new[i][j] = lock[i - keylen + 1][j - keylen + 1]

    for r in range(4):
        for i in range(keylen + locklen - 1):
            for j in range(keylen + locklen - 1):
                temp = copy.deepcopy(new)

                for k in range(keylen):
                    for l in range(keylen):
                        temp[i + k][j + l] += key[k][l]

                flag = 1
                for k in range(keylen - 1, keylen + locklen - 1):
                    for l in range(keylen - 1, keylen + locklen - 1):
                        if temp[k][l] != 1:
                            flag = 0
                            break
                    if flag == 0:
                        break
                if flag == 1:
                    return True

        key = list(zip(*list(reversed(key))))

    return False
