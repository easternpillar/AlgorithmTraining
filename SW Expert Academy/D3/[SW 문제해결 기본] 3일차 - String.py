# Problem:
# Print how many times the string appears in the given sentence.

# My Solution:
answer = []
for i in range(10):
    tn = int(input())
    toFind = input()
    fromString = input()
    answer.append(fromString.count(toFind))

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
