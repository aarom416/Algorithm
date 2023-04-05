#시간 초과 - 문자열을 추가하는 부분이 시간을 많이 잡아먹고 계속해서 check 문자열에 값과 같은 값이 있는 지(O(N)) 비교하기 때문에 시간 초과가 난 것으로 예상
import sys
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
s=''
check=""
flag=True
def dfs(x):
    global s,flag
    visited[x]=True
    if x!=1: #1이 아닌 수들만 문자로 바꿔 늘려감
        s+=str(x)
    if len(graph[x])==1: #자식 노드가 없는 경우
        if s in check: #자식노드들이 check 순서대로 있는 경우
            s=""
        else:
            flag=False #순서대로 있지 않으면 리턴
            return
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
ans=list(map(int,input().split()))
for i in ans:
    check+=str(i) #문자열로 만들어줌
if ans[0]==1:
    dfs(1)
    if flag:
        print(1)
    else:
        print(0) 
else:
    print(0)

#다른 풀이(참조)
import sys
from collections import deque
sys.setrecursionlimit(100000)
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
def dfs():
    x=ans.popleft() #제일 앞에 있는 숫자 뽑기 -> 현재 부모 노드
    if not ans: #리스트가 다 비면 올바른 순환이라는 의미
        print(1)
        exit()
    visited[x]=True
    for _ in range(len(graph[x])): #현재 부모 노드와 연결된 자식 노드 개수만큼 루프 돌면서 
        if ans[0] in graph[x] and not visited[ans[0]]: #자식노드가 맞는지 확인 
            dfs()
    return False #만약 자식노드가 아니라면 재귀 돌다가 False 리턴
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
ans=deque(map(int,input().split())) #맨 앞 값을 popleft 하여 사용하기 위해 deque 선언
if ans[0]==1:
    if not dfs():
        print(0)
else:
    print(0)
