import sys,math

input = sys.stdin.readline

n = int(input())

edges = []
for i in range(n):
    planet = list(map(int,input().split()))
    for j in range(len(planet)):
        edges.append((planet[j],i,j))
edges.sort(reverse=True)
parents = [i for i in range(n)]
def find(x):
    if x!=parents[x]:    
        parents[x] = find(parents[x])
    return parents[x]
def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parents[y]=x
    else:
        parents[x]=y

result=0
while edges:
    w,a,b = edges.pop()
    if find(a)!=find(b):
        union(a,b)
        result+=w
print(result)
    


