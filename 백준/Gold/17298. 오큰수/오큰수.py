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