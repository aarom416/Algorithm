import sys

input = sys.stdin.readline

n = int(input())

xList = []
yList = []
zList = []
for i in range(n):
    x,y,z = map(int,input().split())
    xList.append((x,i))
    yList.append((y,i))
    zList.append((z,i))    
xList.sort()
yList.sort()
zList.sort()
edges=[]
for curList in xList,yList,zList:
    for i in range(1,n):
        w1,a=curList[i-1]
        w2,b=curList[i]
        edges.append((abs(w1-w2),a,b))
edges.sort(reverse=True)
parents = [i for i in range(n+1)]
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parents[y]=x
    else:
        parents[x]=y

count=0
result=0
while count!=n-1:        
    w,a,b = edges.pop()
    if find(a) != find(b):
        union(a,b)
        count+=1
        result+=w
print(result)