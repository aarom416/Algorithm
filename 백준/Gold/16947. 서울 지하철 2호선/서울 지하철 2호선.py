import sys
from collections import deque
input = sys.stdin.readline

# 사이클에 속한 노드부터 BFS 탐색으로 나머지 노드의 거리를 구함
def BFS():
    que = deque()

    for i in range(N):
        if parents[i] == -1:
            answer[i] = 0
            que.append(i)

    while que:
        current = que.popleft()

        for child in graph[current]:
            if answer[child] == -1:
                answer[child] = answer[current] + 1
                que.append(child)


N = int(input())
# 입력받은 그래프 저장
graph = [[] for _ in range(N)]
# graph는 추후 BFS 탐색때 사용해야하므로, 노드를 제거할 별도의 그래프
temp = [[] for _ in range(N)]
# 간선 수를 저장할 변수
graph_size = [0] * N
# 부모 노드를 저장할 변수
parents = [-1] * N
# 출력될 답을 저장할 변수 (거리)
answer = [-1] * N

# 입력 처리
for _ in range(N):
    s1, s2 = map(int, input().split())
    graph[s1-1].append(s2-1)
    temp[s1-1].append(s2-1)
    graph_size[s1-1] += 1
    graph[s2-1].append(s1-1)
    temp[s2-1].append(s1-1)
    graph_size[s2-1] += 1

# 전체 탐색 후 간선 수가 1인 노드가 발견되지 않으면 반복 종료
while True:
    flag = True
    for i in range(N):
        if graph_size[i] == 1:
            parent = temp[i].pop()
            parents[i] = parent
            temp[parent].remove(i)
            graph_size[i] = 0
            graph_size[parent] -= 1
            flag = False

    if flag:
        break

BFS()

print(*answer)