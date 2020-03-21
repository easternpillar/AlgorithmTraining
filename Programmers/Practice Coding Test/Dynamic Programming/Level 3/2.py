# Problem:
# Given the number of tiles, Return the circumference length of the tile.
# Condition(s):
# 1. The tile ornament was made with a square tile, starting with a square tile with one side, and gradually adding larger tiles.

# My Solution:
def solution(N):
    x = y = 1
    for i in range(1, N):
        if i % 2 == 0:
            x += y
        else:
            y += x
    answer = 2 * (x + y)
    return answer
