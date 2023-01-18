import sys
from collections import Counter #counter 모듈을 사용하여 시간 절약
n = int(sys.stdin.readline())
num = [(int(sys.stdin.readline().rstrip())) for _ in range(n)]
num.sort() #입력값 오름차순 정렬
print(round(sum(num)/n)) #산술평균 
print(num[n//2]) #중앙값
num_list = Counter(num).most_common() #가장 많은 것부터 출력 ex)[(-3,2),(-1,1)...]-> -3 2개 -1 1개
if len(num_list)>1: 
    if num_list[0][1]==num_list[1][1]: #최빈값이 2개인 경우
        print(num_list[1][0]) #두번째 최빈값 출력
    else: #최빈값 1개인 경우
        print(num_list[0][0])
else:
    print(num_list[0][0]) 
print(num[-1]-num[0]) #범위 출력