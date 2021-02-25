# Problem:
# Print the average excluding the maximum and minimum values.

# My Solution:
T = int(input())
for i in range(T):
    temp = list(map(int, input().split()))
    print("#{}".format(i + 1), end=" ")
    print(int(round((sum(temp) - max(temp) - min(temp)) / (len(temp) - 2),0)))
