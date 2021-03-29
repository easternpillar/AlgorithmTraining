# Problem:
# Given the volume of a bag and the volumes and values of things, print the maximum value can be gotten.

# My Solution:
T = int(input())
Ns = []
for tc in range(T):
    N, K = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]
    Ns.append((N, K, items))

results = []

for tc in range(T):
    N, K, items = Ns[tc]
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, len(dp)):
        v, c = items[i - 1]
        for j in range(1, len(dp[i])):

            if j >= v:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - v] + c)
            else:
                dp[i][j] = dp[i - 1][j]

    results.append(dp[-1][-1])

for tc in range(T):
    print("#{} {}".format(tc + 1, results[tc]))
