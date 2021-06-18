# Algorithm Training
This repository is for training my algorithm skills.
The language I use is Python3.

## Newly Learned
### String
+ .startswith/endswith(str): 문자열이 str로 시작하는지/끝나는지 boolean 값 반환
+ .replace(str1, str2): str1을 찾아 str2로 대체
+ .rjust/ljust(width, [fillchar]): 문자열 오른쪽/왼쪽 정렬
+ %: ('%d %s %f' %(integer value, string value, floating number value))
+ {}: '{}'.format(value)

### Sys
+ .stdin.readline(): sys 입력
+ .exit(): 프로그램 종료
+ .setrecursionlimit(): 재귀 호출 횟수 지정

### ASCII
+ chr(ascii): 아스키코드를 문자로 변환
+ ord(chr): 문자 chr을 아스키코드로 변환

### Math
+ .inf: 무한대

### Set
+ set(): immutable 자료형를 집합으로 변환
+ .union(): 합집합
+ .intersection(): 교집합
+ .remove(): 집합에 속한 원소 제거 (집합에 해당 원소가 없으면 오류)
+ .discard(): 집합에 해당 원소가 있다면 제거

### Collections
#### Deque
+ .deque(list): 데크로 변환

#### Counter
+ .most_common(): (원소, 빈도수)를 빈도수 내림차순으로 반환

### Heapq
+ .heapify(list): 힙큐로 변환
+ .heappush(heap_list, eli): push
+ .heappop(heap_list): pop

### Base Conversion
+ bin(): 2진수 변환
+ oct(): 8진수 변환
+ hex(): 16진수 변환

### Copy
+ .deepcopy(): 인스턴스 완전 복사

### Itertools
+ .permutations(): 순열
+ .combinations(): 조합
+ .combinations_with_replacement(): 중복 조합
+ .product(): 데카르트 곱


### Dictionary
.get(key, default): key값이 있는 경우 value, 없는 경우 default 반환

### Etc.
+ enumerate(): 순서 지정
+ *: 언패킹
+ zip(): 이터러블 집계
+ for else문: for문 블록이 완전히 수행됐을 때 else문에 진입

## Review Needed
### Programmers
#### Level 2
+ Summer/Winter Coding(2019) [멀쩡한 사각형](https://programmers.co.kr/learn/courses/30/lessons/62048)
+ Exercise [124나라의 숫자](https://programmers.co.kr/learn/courses/30/lessons/12899)
+ Exercise [가장 큰 정사각형 찾기](https://programmers.co.kr/learn/courses/30/lessons/12905)

#### Level 3
+ Greedy [저울](https://programmers.co.kr/learn/courses/30/lessons/42886)
+ Dynamic Programming [N으로 표현](https://programmers.co.kr/learn/courses/30/lessons/42895)
+ Exercise [2 x n 타일링](https://programmers.co.kr/learn/courses/30/lessons/12900)
+ 2020 KAKAO BLIND RECRUITMENT [기둥과 보 설치](https://programmers.co.kr/learn/courses/30/lessons/60061)
+ 2020 KAKAO BLIND RECRUITMENT [외벽 점검](https://programmers.co.kr/learn/courses/30/lessons/60062)
+ Exercise [거스름돈](https://programmers.co.kr/learn/courses/30/lessons/12907)
+ Exercise [하노이의 탑](https://programmers.co.kr/learn/courses/30/lessons/12946)
+ Exercise [N-Queen](https://programmers.co.kr/learn/courses/30/lessons/12952)
+ 2020 KAKAO INTERNSHIP [[카카오 인턴] 보석 쇼핑](https://programmers.co.kr/learn/courses/30/lessons/67258)
+ Summer/Winter Coding(~2018) [배달](https://programmers.co.kr/learn/courses/30/lessons/12978)
+ 2020 KAKAO INTERNSHIP [경주로 건설](https://programmers.co.kr/learn/courses/30/lessons/67259)
+ Summer/Winter Coding(~2018) [기지국 설치](https://programmers.co.kr/learn/courses/30/lessons/12979)
+ 2019 KAKAO BLIND RECRUITMENT [길 찾기 게임](https://programmers.co.kr/learn/courses/30/lessons/42892)
+ Monthly Code Challenge Season 1 [스타 수열](https://programmers.co.kr/learn/courses/30/lessons/70130)
+ 2021 KAKAO BLIND RECRUITMENT [카드 짝 맞추기](https://programmers.co.kr/learn/courses/30/lessons/72415)
+ 2021 KAKAO BLIND RECRUITMENT [합승 택시 요금](https://programmers.co.kr/learn/courses/30/lessons/72413)

#### Level 4
+ Dynamic Programming [카드 게임](https://programmers.co.kr/learn/courses/30/lessons/42896)

### Baekjoon
#### 삼성 SW 역량 테스트 기출 문제
+ [퇴사](https://www.acmicpc.net/problem/14501)
+ [사다리 조작](https://www.acmicpc.net/problem/15684)
+ [드래곤 커브](https://www.acmicpc.net/problem/15685)
+ [나무 재테크](https://www.acmicpc.net/problem/16235)
+ [아기 상어](https://www.acmicpc.net/problem/16236)

#### 동적계획법 2
+ [동전](https://www.acmicpc.net/problem/9084)
+ [평범한 배낭](https://www.acmicpc.net/problem/12865)

#### 분리집합
+ [집합의 표현](https://www.acmicpc.net/problem/1717)

#### 위상정렬
+ [선수과목 (Prerequisite)](https://www.acmicpc.net/problem/14567)
+ [ACM Craft](https://www.acmicpc.net/problem/1005)

#### 최소 스패닝 트리
+ [최소 스패닝 트리](https://www.acmicpc.net/problem/1197)

#### 트리 디피
+ [트리와 쿼리](https://www.acmicpc.net/problem/15681)

#### 시뮬레이션
+ [미세먼지 안녕!](https://www.acmicpc.net/problem/17144)

#### 자료구조 2
+ [이중 우선순위 큐](https://www.acmicpc.net/problem/7662)

#### 이분탐색
+ [나무 자르기](https://www.acmicpc.net/problem/2805)

### SW Expert Academy
#### D3
+ [제곱수](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXWXH_h695kDFAST&categoryId=AXWXH_h695kDFAST&categoryType=CODE)
+ [새샘이와 세 소수](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWaJ3q8qV-4DFAUQ&categoryId=AWaJ3q8qV-4DFAUQ&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=3)
+ [이진 문자열 복원](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWUiwoe6o00DFAVT)
+ [재미있는 오셀로 게임](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWQmA4uK8ygDFAXj&categoryId=AWQmA4uK8ygDFAXj&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=4)
+ [승률 비교하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWIX_iFqjg4DFAVH&categoryId=AWIX_iFqjg4DFAVH&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=5)
+ [최장 공통 부분 수열](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWBOHEx66kIDFAWr&categoryId=AWBOHEx66kIDFAWr&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6)
+ [0&1 Knapsack](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWBJAVpqrzQDFAWr&categoryId=AWBJAVpqrzQDFAWr&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6)
+ [홍준이의 숫자 놀이](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV-0U8FKZLQDFAXT&categoryId=AV-0U8FKZLQDFAXT&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6)
+ [[S/W 문제해결 응용] 2일차 - 최대상금](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8)
+ [[S/W 문제해결 응용] 1일차 - 단순 2진 암호코드](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15FZuqAL4CFAYD&categoryId=AV15FZuqAL4CFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8)
+ [[Professional] 조합](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWXGKdbqczEDFAUo&categoryId=AWXGKdbqczEDFAUo&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9)

## Not Solved
### SW Expert Academy
+ [다트 게임](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXZuaLsqz9wDFAST)
+ [마법사 상어와 블리자드](https://www.acmicpc.net/problem/21611)

## Pre-learning Material(s)
+ [파이썬을 파이썬답게](https://programmers.co.kr/learn/courses/4008)
+ [[라이브 강의] 이것이 취업을 위한 코딩 테스트다 with Python](https://www.youtube.com/playlist?list=PLRx0vPvlEmdBFBFOoK649FlEMouHISo8N)
