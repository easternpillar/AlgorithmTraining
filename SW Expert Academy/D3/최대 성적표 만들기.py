# Problem:
# When adding up the grades by the given number, print the maximum total score.

# My Solution:
T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    score = sorted(list(map(int, input().split())), reverse=True)
    print("#{} {}".format(i + 1, sum(score[:K])))
