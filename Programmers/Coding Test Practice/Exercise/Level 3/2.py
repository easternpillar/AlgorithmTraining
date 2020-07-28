# Problem:
# Given a string, return the longest palindrome.

# My Solution:
def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(len(s) - 1, i - 1, -1):
            if s[j] == s[i]:
                left = i
                right = j
                flag = 1
                if j - i + 1 < answer:
                    continue
                while left < right:
                    left += 1
                    right -= 1
                    if s[left] != s[right]:
                        flag = 0
                        break

                if flag == 1 and j - i + 1 > answer:
                    answer = j - i + 1

            else:
                continue
    return answer
