# Problem:
# Given the word to find and the information of web pages, return the index of the webpage that has the highest matching points.
# Condition(s):
# 1. The word is not case-sensitive.
# 2. The final score is the sum of the base score and the link score.
# 3. The base score is the number of occurrences of the word.
# 4. The link score is the sum of the basic score ÷ number of external links of other web pages linked to the web page.
# 5. The URL is given as the value of the <meta> tag in the <head> tag of HTML.
# 6. External links have the form <a href= />.
# 7. All urls start only with https://.
# 8. Words are separated by all other characters except the alphabet.

# My Solution:
def solution(word, pages):
    answer = 0
    word = word.lower()

    urls = []
    refs = [[] for _ in range(len(pages))]
    score = [0 for _ in range(len(pages))]
    total = [0 for _ in range(len(pages))]
    for i in range(len(pages)):
        pages[i] = pages[i].lower()
        urls.append(pages[i][pages[i].find('<meta property="og:url" content="https://') + 33:pages[i].find('/>', pages[
            i].find('<meta property="og:url" content="https://')) - 1])
        print(urls)
        idx = -1
        while idx < len(pages[i]) - 1:
            nidx = pages[i].find('<a href=', idx + 1)
            if nidx == -1:
                break
            refs[i].append(pages[i][nidx + 9:pages[i].find('>', nidx) - 1])
            idx = nidx

        sidx = pages[i].find('<body>') + 5
        fidx = pages[i].find('</body>') - 1

        while sidx < fidx:
            nidx = pages[i].find(word, sidx + 1)
            if nidx == -1:
                break
            if not pages[i][nidx + len(word)].isalpha() and not pages[i][nidx - 1].isalpha():
                score[i] += 1
            sidx = nidx

    for i in range(len(urls)):
        total[i] += score[i]
        for j in range(len(urls)):
            if i == j:
                continue
            if urls[i] in refs[j]:
                total[i] += score[j] / len(refs[j])

    m = 0
    for i in range(len(total)):
        if total[i] > m:
            m = total[i]
            answer = i
    return answer
