import sys,math

input = sys.stdin.readline

n,m = map(int,input().split())

planet = [list(map(int,input().split())) for _ in range(n)]
connect_planet = [list(map(int,input().split())) for _ in range(m)]

connect = [False]*(n+1)
edges = []
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
        
for x,y in connect_planet:
    union(x,y)

k = len(planet)
for i in range(k-1):
    for j in range(i+1,k):
        dist = math.sqrt(abs(planet[i][0]-planet[j][0])**2+abs(planet[i][1]-planet[j][1])**2)
        edges.append((dist,i+1,j+1))
edges.sort(reverse=True)
        
result=0
while edges:
    w,a,b = edges.pop()
    if find(a) != find(b):
        union(a,b)
        result+=w
result = round(result,2)
print(format(result,".2f"))