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