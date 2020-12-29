# Problem:
# Print the grade of the nth student.
# Condition(s):
# 1. Grades are given in order of total score.
# 2. The total score is calculated by adding up 35% of the midterm score, 45% of the final test score, and 20% of the assignment score.
# 3. The same grade can be given as the number of students/10.

# My Solution:
T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    print("#{}".format(i + 1), end=" ")
    score = []
    for j in range(N):
        mid, final, assignment = map(int, input().split())
        score.append([j + 1, mid * 0.35 + final * 0.45 + assignment * 0.20])
        score.sort(key=lambda x: -x[1])

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    same = N // 10
    idx = 0
    for j in range(N):
        score[j][1] = grade[idx]
        same -= 1
        if same == 0:
            same = N // 10
            idx += 1

    for j in range(N):
        if score[j][0] == K:
            print(score[j][1])
