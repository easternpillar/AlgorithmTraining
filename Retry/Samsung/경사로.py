# Reference: https://www.acmicpc.net/problem/14890
import sys

N, L = map(int, sys.stdin.readline().split())
routes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0


def rotate(routes):
    return list(zip(*routes))


for _ in range(2):
    for route in routes:
        idx = 0
        prev = route[idx]
        cnt = 0
        flag = True
        while idx < len(route):
            if route[idx] == prev:
                cnt += 1
            elif route[idx] == prev + 1:
                if cnt >= L:
                    cnt = 1
                else:
                    flag = False
                    break
            elif route[idx] == prev - 1:
                prev = route[idx]
                cnt = 0
                while idx < len(route):
                    if route[idx] == prev:
                        cnt += 1
                        if cnt >= L:
                            break
                    else:
                        flag = False
                        break
                    idx += 1
                if not flag:
                    break
                if cnt < L:
                    flag = False
                    break
                cnt = 0
            else:
                flag = False
                break
            prev = route[idx]
            idx += 1
        if flag:
            answer += 1
    routes = rotate(routes)
print(answer)
