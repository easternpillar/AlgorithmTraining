# Problem:
# When counting multiples of a given number,print at least how many times you'll see all the numbers from 0 to 9 in the number of digits you've seen before.

# My Solution:
T = int(input())
for i in range(T):
    N = int(input())
    s = set()
    print("#{}".format(i + 1), end=" ")
    m = 1
    while True:
        s = s.union(list(str(N * m)))
        if len(s) == 10:
            print(N * m)
            break
        m += 1
