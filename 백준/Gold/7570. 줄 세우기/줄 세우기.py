        
import sys

input = sys.stdin.readline

n = int(input().rstrip())

childrens = list(map(int,input().split()))
children_loc = [-1]*(n+1)
for idx, children in enumerate(childrens):
    children_loc[children] = idx 

count=1
result=0
for i in range(1,n):
    if children_loc[i] < children_loc[i+1]:
        count+=1
    else:
        result = max(result,count)
        count=1

print(n-result if n != 1 else 0)