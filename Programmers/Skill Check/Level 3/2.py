# Problem:
# Given the routes of cars using highway, return the minimum number of cameras satisfying that all cars meet one camera at least.

# My Solution:
def solution(routes):
    answer = len(routes)
    routes.sort(reverse=True)
    print(routes)

    l, r = routes.pop()

    while routes:
        temp_l, temp_r = routes.pop()

        if l <= temp_l <= r:
            answer -= 1
            if temp_r <= r:
                l, r = temp_l, temp_r
        else:
            l, r = temp_l, temp_r
    return answer
