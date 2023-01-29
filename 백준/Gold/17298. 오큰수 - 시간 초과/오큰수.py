#시간 초과 - worst case 경우 O(n^2) 걸림
import sys
from collections import deque
n = int(sys.stdin.readline())
num_deque = deque(list(map(int,sys.stdin.readline().split())))
NGE=list()
while len(num_deque):
    number = num_deque.popleft() #제일 왼쪽부터 popleft 하고 저장하여 나머지 숫자와 비교
    idx=0
    while True:
        if idx<len(num_deque) and num_deque[idx]>number:
            NGE.append(num_deque[idx])
            break
        elif idx==len(num_deque): #비교할 숫자가 없으면(=마지막 숫자) -1 출력
            NGE.append(-1)
            break
        else:
            idx+=1
for i in NGE:
    print(i,end=" ")

#다른 풀이 - stack에 인덱스 번호를 넣고 반복 탐색
import sys
n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
nge=[-1]*n
stack=[] #인덱스 번호를 넣을 stack
stack.append(0)
for i in range(1,n):
    while stack and num_list[stack[-1]]<num_list[i]: #i번쨰 숫자가 크면
        nge[stack.pop()]=num_list[i] #stack에서 pop하여 인덱스 번호에 해당 숫자 저장 반복
    stack.append(i) #인덱스 기억
print(*nge)
