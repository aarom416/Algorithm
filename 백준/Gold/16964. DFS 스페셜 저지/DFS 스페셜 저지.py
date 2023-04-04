import sys
from collections import deque
sys.setrecursionlimit(100000)


def dfs(graph, visited, cmp, start):
    tmp = cmp.popleft()
    if not cmp:
        print(1)
        exit(0)
    visited[tmp] = True
    for i in range(len(graph[tmp])):
        if cmp[0] in graph[tmp] and not visited[cmp[0]]:
            dfs(graph, visited, cmp, cmp[0])
    return False


N = int(sys.stdin.readline())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(1, N):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

cmp = deque(map(int, sys.stdin.readline().split()))
if cmp[0] != 1:
    print(0)
    exit(0)
if not dfs(graph, visited, cmp, 1):
    print(0)