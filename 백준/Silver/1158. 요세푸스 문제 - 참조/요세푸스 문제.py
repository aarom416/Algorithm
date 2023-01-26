import sys
n,k = map(int,sys.stdin.readline().split())
delete_list=[]
num_list=list(range(1,n+1))
idx=0
for _ in range(n):
    idx+=k-1 #인덱스 번호 저장
    if idx>=len(num_list): #인덱스 번호가 
        idx = idx%len(num_list)
    delete_list.append(str(num_list.pop(idx))) #삭제한 수 저장
print(f"<{', '.join(delete_list)}>")

#다른 풀이 - deque 활용
from collections import deque
import sys
n,k = map(int,sys.stdin.readline().split())
delete_list=[]
num_list=deque(range(1,n+1))
while num_list:
    for _ in range(k-1): 
        num_list.append(num_list.popleft())#k-1까지 앞에 번호 pop하고 뒤에 다시 연결
    delete_list.append(num_list.popleft()) #k번째의 수 pop
print(str(delete_list).replace('[','<').replace(']','>'))
