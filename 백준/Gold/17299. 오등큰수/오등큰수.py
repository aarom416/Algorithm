from collections import Counter
import sys
n = int(sys.stdin.readline().rstrip())
num_list=list(map(int,sys.stdin.readline().split()))
num_count=Counter(num_list)
res=[-1]*len(num_list)
stack=[0] #인덱스를 저장할 stack
for i in range(1,n):
    while stack and num_count[num_list[stack[-1]]]<num_count[num_list[i]]:
        res[stack.pop()]=num_list[i]
    stack.append(i)
print(*res)
