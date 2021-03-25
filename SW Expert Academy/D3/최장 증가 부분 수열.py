# Problem:
# Print the length of the longest incremental partial sequence.

# My Solution:
for i in range(int(input())):
    N = int(input())
    eli = list(map(int,input().split()))
    dp = [1 for _ in range(len(eli))]
    for j in range(len(eli)):
        for k in range(j - 1, -1, -1):
            if eli[k] <= eli[j]:
                dp[j] = max(dp[j], dp[k] + 1)
    print("#{} {}".format(i + 1, max(dp)))
