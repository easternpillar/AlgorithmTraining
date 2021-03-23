# Problem:
# When you convert a score less than 40 to 40, print the average score.

# My Solution:
answer = []

for i in range(int(input())):
    score = list(map(int, input().split()))
    cnt = 0
    for j in range(len(score)):
        if score[j] < 40:
            score[j] = 40

    answer.append(sum(score) // len(score))

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
