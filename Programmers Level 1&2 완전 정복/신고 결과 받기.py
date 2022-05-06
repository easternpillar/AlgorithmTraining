# 링크: https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3
# 문제 접근
# 1. 딕셔너리에 나를 신고한 사람의 이름을 담음
# 2. 딕셔너리 길이가 기준을 넘으면 딕셔너리 values에게 메일이 전송
# 3. 딕셔너리 value값은 중복되면 안되므로 set

from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report_dict = defaultdict(set)
    cnt_dict = defaultdict(int)
    for re in report:
        a, b = re.split(" ")
        report_dict[b].add(a)

    for key in report_dict:
        if len(report_dict[key]) >= k:
            for value in report_dict[key]:
                cnt_dict[value] += 1

    for id in id_list:
        answer.append(cnt_dict[id])

    return answer

