import sys

input = sys.stdin.readline

v,e = map(int,input().split())

nodes = [list(map(int,input().split())) for _ in range(e)]

nodes.sort(key=lambda x:x[2])
parent = [i for i in range(v+1)]

result=0

def find(x):
    if x!=parent[x]: #연결되어 있는 부모 노드 찾기 
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y
        
for start, end, value in nodes:
    if find(start) != find(end): #연결되어 있지 않은 경우
        union(start,end) #합치기
        result+=value
print(result)