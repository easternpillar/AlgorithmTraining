# Problem:
# Print the minimum number of currencies for change.

# My Solution:
T = int(input())
for i in range(T):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0 for _ in range(8)]
    print("#{}".format(i+1))
    for j in range(8):
        q, r = divmod(N, money[i])
        N = r
        print(q, end=" ")
    print("")
