#시간 초과
import sys
n = int(sys.stdin.readline())
num = [(int(sys.stdin.readline().rstrip())) for _ in range(n)]
num.sort() #입력값 오름차순 정렬
print(round(sum(num)/n)) #산술평균 
print(num[int(n//2)]) #중앙값
num_list = []
cnt=0
for i in set(num): #입력값 개수 리스트에 넣음
    num_list.append(num.count(i))
if n==1: #입력값 하나인 경우
    print(num[0])
else:
    if max(num_list)==1: #입력값 최대 개수가 1이면
        print(num[1]) #두번째 리스트값 출력
    for i in range(len(num_list)): 
        if num_list[i]==max(num_list): #최대 개수와 각 리스트에 있는 개수 비교
            cnt+=1 #최빈값 개수 카운트
            idx = i #인덱스 번호 기억
            if cnt==2:
                break
    if cnt<=2: #최빈값 중 두번쨰로 작은 값을 출력해야 하므로 최빈값 개수가 2개 이하이면
        print(num[sum(num_list[:idx+1])-1]) # idx까지의 인덱스합(idx까지의 리스트 총 개수)을 인덱스로 갖는 입력값 리스트 출력
print(max(num)-min(num)) #범위 출력

#다른 풀이(Counter 모듈 사용)

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
