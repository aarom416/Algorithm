# BFS

## 1. BFS란?

BFS(Breadth-First Search, 너비 우선 탐색)는 **그래프 탐색 알고리즘**이다. 시작 정점에서 가까운 정점부터 같은 거리 단위로 넓게 탐색하며, 간선의 비용이 모두 같다면 최단 거리를 보장한다.

BFS는 큐를 사용한다. 먼저 발견한 정점을 큐에 넣고, 큐에서 꺼낸 정점의 연결 정점을 다시 큐에 넣는다.

## 2. 왜 BFS를 사용하는가?

간선의 비용이 모두 1이거나 모든 이동이 같은 횟수라면 BFS는 방문 순서 자체가 시작점에서의 거리 순서가 된다.

따라서 미로에서 최소 이동 횟수를 구하거나, 그래프에서 특정 정점까지의 최단 간선 수를 구할 때 적합하다.

다익스트라는 가중치가 다른 그래프에서도 사용할 수 있지만 우선순위 큐가 필요하다. 모든 간선 비용이 같다면 BFS가 더 간단하고 빠르다.

| 상황 | 적합한 알고리즘 |
|---|---|
| 간선 비용이 모두 같음 | BFS |
| 간선 비용이 0 이상이고 서로 다름 | 다익스트라 |
| 깊이 방향으로 끝까지 탐색 | DFS |
| 모든 정점 쌍의 최단 거리 | 플로이드 워셜 |

## 3. 어떤 코테 문제에서 BFS를 의심해야 할까?

- 미로, 격자, 지도에서 최소 이동 횟수를 구한다.
- 시작점에서 목표점까지 몇 번 이동해야 하는지 묻는다.
- 간선 또는 이동 비용이 모두 1이다.
- 현재 위치에서 상하좌우, 또는 인접 정점으로 이동한다.
- 같은 거리의 위치를 먼저 모두 확인해야 한다.
- “최소 횟수”, “가장 가까운”, “몇 단계 만에 도착”이라는 표현이 나온다.

정점 수가 크고 간선 비용이 모두 같다면 `O(V + E)`인 BFS를 먼저 생각한다.

## 4. BFS 탐색 흐름

다음 그래프에서 1번 정점부터 탐색한다고 하자.

```text
        2       5
       / \     /
      1   4 - 6
       \ /     \
        3       7
```

탐색 순서는 다음과 같다.

```text
시작: 큐 [1]

1 방문 → 2, 3 발견 → 큐 [2, 3]
2 방문 → 4 발견     → 큐 [3, 4]
3 방문 → 새로운 정점 없음 → 큐 [4]
4 방문 → 5, 6 발견 → 큐 [5, 6]
```

1번에서 거리가 1인 정점 `2, 3`을 모두 처리한 뒤, 거리 2인 정점 `4`를 처리한다. 이처럼 가까운 정점부터 층별로 탐색한다.

## 5. 큐와 방문 배열

```java
Queue<Integer> queue = new ArrayDeque<>();
boolean[] visited = new boolean[n + 1];

queue.offer(start); // 시작 정점을 큐 뒤에 넣는다.
visited[start] = true; // 큐에 넣을 때 방문 처리한다.

while (!queue.isEmpty()) {
    int current = queue.poll(); // 큐 앞에서 가장 먼저 들어온 정점을 꺼낸다.

    for (int next : graph[current]) {
        if (!visited[next]) {
            visited[next] = true; // 중복해서 큐에 들어가지 않도록 표시한다.
            queue.offer(next); // 다음에 탐색할 정점을 큐 뒤에 넣는다.
        }
    }
}
```

방문 처리는 큐에 넣는 순간 하는 것이 안전하다. 꺼낼 때 방문 처리하면 같은 정점이 여러 경로에서 큐에 중복으로 들어갈 수 있다.

## 6. Java 그래프 탐색 예시

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int n = 7;
        List<Integer>[] graph = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>(); // 각 정점의 인접 리스트를 만든다.
        }

        addEdge(graph, 1, 2);
        addEdge(graph, 1, 3);
        addEdge(graph, 2, 4);
        addEdge(graph, 3, 4);
        addEdge(graph, 4, 5);
        addEdge(graph, 4, 6);
        addEdge(graph, 6, 7);

        bfs(graph, 1);
        // 출력 예시: 1 2 3 4 5 6 7
    }

    static void addEdge(List<Integer>[] graph, int a, int b) {
        graph[a].add(b);
        graph[b].add(a); // 무방향 그래프이므로 양쪽에 추가한다.
    }

    static void bfs(List<Integer>[] graph, int start) {
        boolean[] visited = new boolean[graph.length];
        Queue<Integer> queue = new ArrayDeque<>();

        queue.offer(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int current = queue.poll();
            System.out.print(current + " ");

            for (int next : graph[current]) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.offer(next);
                }
            }
        }
    }
}
```

인접 리스트가 입력 순서에 따라 달라질 수 있으므로, 방문 순서가 반드시 하나로 고정되는 것은 아니다. 중요한 것은 같은 거리의 정점을 먼저 처리한다는 BFS의 구조이다.

## 7. BFS로 최단 거리 구하기

방문 여부만 저장하지 않고 시작점에서의 거리를 함께 저장하면 최단 이동 횟수를 구할 수 있다.

```java
static int[] shortestDistance(List<Integer>[] graph, int start) {
    int[] distance = new int[graph.length];
    Arrays.fill(distance, -1); // -1은 아직 방문하지 않았다는 뜻이다.

    Queue<Integer> queue = new ArrayDeque<>();
    distance[start] = 0; // 시작점까지 이동 횟수는 0이다.
    queue.offer(start);

    while (!queue.isEmpty()) {
        int current = queue.poll();

        for (int next : graph[current]) {
            if (distance[next] == -1) {
                distance[next] = distance[current] + 1; // 한 번 이동했으므로 1 증가한다.
                queue.offer(next);
            }
        }
    }

    return distance;
}
```

출발점이 1번이고 결과가 다음과 같다면:

```text
distance[1] = 0
distance[2] = 1
distance[3] = 1
distance[4] = 2
```

1번에서 4번까지 최소 2번 이동해야 한다는 뜻이다.

## 8. 격자에서 BFS

미로 문제에서는 정점을 행과 열의 위치로 생각한다.

```java
int[] dr = {-1, 1, 0, 0}; // 위, 아래 이동
int[] dc = {0, 0, -1, 1}; // 왼쪽, 오른쪽 이동

for (int direction = 0; direction < 4; direction++) {
    int nextRow = row + dr[direction];
    int nextCol = col + dc[direction];

    if (nextRow < 0 || nextRow >= rows
            || nextCol < 0 || nextCol >= cols) {
        continue; // 격자 밖이면 이동하지 않는다.
    }

    if (map[nextRow][nextCol] == 0) {
        continue; // 벽이면 이동하지 않는다.
    }
}
```

격자 BFS에서는 다음 네 가지를 항상 확인한다.

1. 다음 위치가 격자 안에 있는가?
2. 벽이나 장애물이 아닌가?
3. 아직 방문하지 않았는가?
4. 이동 횟수를 현재 거리보다 1 크게 기록했는가?

## 9. 시간 복잡도와 공간 복잡도

- 인접 리스트 그래프: `O(V + E)`
- 인접 행렬 그래프: `O(V^2)`
- 큐와 방문 배열: `O(V)`
- 격자 BFS: 격자 칸 수를 `R × C`라고 할 때 `O(R × C)`

각 정점과 간선을 최대 한 번씩 확인하므로 인접 리스트에서는 `O(V + E)`이다.

## 10. 주의할 점

- 방문 처리는 큐에 넣을 때 한다.
- 간선 비용이 서로 다르면 일반 BFS로 최단 거리를 구할 수 없다.
- 방향 그래프인지 무방향 그래프인지 확인한다.
- 연결되지 않은 정점이 있을 수 있으므로 모든 정점을 방문해야 하면 각 정점에서 BFS를 시작하는 방법을 고려한다.
- 격자에서는 행·열 범위 검사를 먼저 한다.
- 최단 경로 자체가 필요하면 부모 정점 배열을 저장해 경로를 역추적한다.

## 11. 학습 문제

- [프로그래머스 - 게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844): 격자에서 목적지까지의 최소 이동 횟수를 구하는 대표적인 BFS 문제이다.
- [프로그래머스 - 가장 먼 노드](https://school.programmers.co.kr/learn/courses/30/lessons/49189): 1번 노드에서 가장 먼 노드의 개수를 구하는 그래프 BFS 문제이다.
- [프로그래머스 - 네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162): 연결된 컴퓨터 그룹의 개수를 BFS 또는 DFS로 구한다.
