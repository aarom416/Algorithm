# DFS

## 1. DFS란?

DFS(Depth-First Search, 깊이 우선 탐색)는 **그래프 탐색 알고리즘**이다. 한 방향으로 갈 수 있을 때까지 깊게 들어간 뒤, 더 이상 갈 수 없으면 이전 정점으로 돌아와 다른 경로를 탐색한다.

DFS는 재귀함수 또는 스택으로 구현한다. 트리의 모든 자식 노드를 깊이 순서로 확인하거나, 연결 요소와 모든 경로를 탐색할 때 자주 사용한다.

## 2. 왜 DFS를 사용하는가?

DFS는 현재 선택한 경로를 끝까지 따라가므로 “한 경로를 완성한 뒤 다음 경로를 시도”하는 문제를 자연스럽게 표현할 수 있다.

- 재귀 구조가 있는 트리와 그래프를 간결하게 탐색할 수 있다.
- 모든 경로, 모든 조합, 백트래킹 문제에 적합하다.
- 연결 요소의 개수와 사이클 여부를 확인할 수 있다.
- 방문한 정점에서 다시 이전 상태로 돌아가는 흐름을 표현하기 쉽다.

BFS는 가까운 정점부터 탐색하며 간선 비용이 같을 때 최단 거리를 보장하지만, DFS는 최단 거리보다 경로 탐색과 구조 확인에 더 적합하다.

## 3. 어떤 코테 문제에서 DFS를 의심해야 할까?

- 연결된 모든 정점이나 모든 영역의 개수를 구한다.
- 한 경로를 끝까지 이동한 뒤 다른 경로를 시도한다.
- 모든 경우의 수, 모든 경로, 가능한 조합을 확인한다.
- 방문한 정점을 다시 돌아와 다른 선택을 해야 한다.
- 섬의 개수, 네트워크 개수, 바이러스 확산 영역 등을 구한다.
- 트리의 순회, 높이, 서브트리 크기, 부모 관계를 구한다.
- 재귀, 깊이, 백트래킹, 경로 탐색이라는 표현이 나온다.

## 4. DFS 탐색 흐름

다음 그래프에서 1번부터 DFS를 시작한다고 하자.

```text
        2       5
       / \     /
      1   4 - 6
       \ /     \
        3       7
```

인접 정점을 작은 번호부터 탐색하면 다음과 같이 한 방향으로 깊게 들어간다.

```text
1 → 2 → 4 → 3
          ↩ 더 갈 곳이 없으므로 4로 돌아감
          ↩ 더 갈 곳이 없으므로 2로 돌아감
2에서 다른 경로 확인
```

정확한 방문 순서는 인접 리스트에 정점을 넣은 순서에 따라 달라진다. DFS의 핵심은 가까운 정점 전체를 먼저 처리하는 것이 아니라, 현재 경로를 끝까지 내려가는 것이다.

## 5. 재귀 DFS

```java
static void dfs(List<Integer>[] graph, boolean[] visited, int current) {
    visited[current] = true; // 현재 정점을 방문 처리한다.
    System.out.print(current + " "); // 방문 순서를 출력한다.

    for (int next : graph[current]) {
        if (!visited[next]) {
            dfs(graph, visited, next); // 다음 정점으로 깊게 들어간다.
        }
    }
}
```

함수를 호출하면 현재 정점의 탐색이 잠시 멈추고 다음 정점의 DFS가 시작된다. 더 이상 방문할 정점이 없으면 함수가 끝나며 이전 호출 위치로 돌아온다. 이 과정을 **백트래킹 또는 되돌아오기**라고 이해할 수 있다.

## 6. Java 재귀 DFS 예시

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int n = 7;
        List<Integer>[] graph = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        addEdge(graph, 1, 2);
        addEdge(graph, 1, 3);
        addEdge(graph, 2, 4);
        addEdge(graph, 3, 4);
        addEdge(graph, 4, 5);
        addEdge(graph, 4, 6);
        addEdge(graph, 6, 7);

        boolean[] visited = new boolean[n + 1];
        dfs(graph, visited, 1);
        // 출력 예시: 1 2 4 3 5 6 7
    }

    static void addEdge(List<Integer>[] graph, int a, int b) {
        graph[a].add(b);
        graph[b].add(a); // 무방향 그래프이므로 양쪽에 추가한다.
    }

    static void dfs(List<Integer>[] graph, boolean[] visited, int current) {
        visited[current] = true;
        System.out.print(current + " ");

        for (int next : graph[current]) {
            if (!visited[next]) {
                dfs(graph, visited, next);
            }
        }
    }
}
```

인접 리스트의 순서에 따라 출력은 달라질 수 있지만, 방문한 정점을 다시 방문하지 않는다는 점은 같다.

## 7. 스택으로 구현하는 DFS

재귀 호출 대신 직접 `Stack` 역할을 하는 `Deque`를 사용할 수도 있다.

```java
static void dfsIterative(List<Integer>[] graph, int start) {
    boolean[] visited = new boolean[graph.length];
    Deque<Integer> stack = new ArrayDeque<>();

    stack.push(start); // 가장 먼저 시작 정점을 스택에 넣는다.

    while (!stack.isEmpty()) {
        int current = stack.pop(); // 가장 최근에 넣은 정점을 꺼낸다.

        if (visited[current]) {
            continue; // 이미 방문했다면 건너뛴다.
        }

        visited[current] = true;
        System.out.print(current + " ");

        for (int next : graph[current]) {
            if (!visited[next]) {
                stack.push(next); // 나중에 넣은 정점이 먼저 탐색된다.
            }
        }
    }
}
```

재귀 DFS는 호출 스택을 사용하고, 반복형 DFS는 직접 만든 스택을 사용한다. 탐색 원리는 같다.

## 8. 연결 요소 개수 구하기

그래프가 여러 덩어리로 나뉘어 있을 때, 방문하지 않은 정점에서 DFS를 새로 시작하면 연결 요소를 셀 수 있다.

```java
int componentCount = 0;
boolean[] visited = new boolean[n + 1];

for (int node = 1; node <= n; node++) {
    if (!visited[node]) {
        componentCount++;
        dfs(graph, visited, node); // 하나의 연결된 덩어리를 모두 방문한다.
    }
}

System.out.println(componentCount); // 연결 요소의 개수
```

## 9. 백트래킹과 DFS

모든 경우의 수를 탐색하는 문제에서는 DFS를 진행하면서 선택하고, 재귀호출이 끝난 뒤 선택을 취소한다.

```java
static void search(int depth) {
    if (depth == targetDepth) {
        return; // 하나의 선택 경로가 완성되면 종료한다.
    }

    for (int choice = 0; choice < n; choice++) {
        if (used[choice]) {
            continue;
        }

        used[choice] = true; // 선택한다.
        search(depth + 1); // 다음 깊이로 내려간다.
        used[choice] = false; // 돌아온 뒤 선택을 취소한다.
    }
}
```

`used[choice] = false`가 있어야 다음 경로에서 해당 선택을 다시 사용할 수 있다. 이것이 DFS 기반 백트래킹의 핵심이다.

## 10. BFS와 비교

| 구분 | DFS | BFS |
|---|---|---|
| 탐색 방식 | 한 경로를 끝까지 탐색 | 같은 거리의 정점을 먼저 탐색 |
| 자료구조 | 재귀 또는 스택 | 큐 |
| 최단 거리 | 일반적으로 보장하지 않음 | 간선 비용이 같으면 보장 |
| 대표 문제 | 연결 요소, 모든 경로, 백트래킹 | 최소 이동 횟수, 레벨 탐색 |

최단 이동 횟수가 필요한데 모든 간선 비용이 같다면 BFS를 우선 고려한다. 모든 경로를 확인하거나 깊이별 선택을 해야 한다면 DFS를 고려한다.

## 11. 시간 복잡도와 공간 복잡도

- 인접 리스트 DFS: `O(V + E)`
- 방문 배열: `O(V)`
- 재귀 호출 스택 또는 명시적 스택: 최대 `O(V)`
- 격자 DFS: 행과 열이 `R`, `C`라면 `O(R × C)`

각 정점과 간선을 최대 한 번씩 확인하므로 인접 리스트에서는 `O(V + E)`이다.

## 12. 주의할 점

- 방문 처리를 하지 않으면 사이클에서 무한히 반복할 수 있다.
- 재귀 깊이가 깊으면 스택 오버플로가 발생할 수 있다.
- 방향 그래프인지 무방향 그래프인지 확인한다.
- 모든 정점을 확인해야 한다면 모든 정점을 시작점으로 순회한다.
- 최단 거리 문제에서 가중치가 같지 않다면 DFS를 사용하면 안 된다.
- 백트래킹에서는 재귀호출 뒤 선택을 반드시 원상 복구한다.

## 13. 학습 문제

- [프로그래머스 - 네트워크](https://school.programmers.co.kr/learn/courses/30/lessons/43162): 연결된 컴퓨터 그룹의 개수를 DFS로 구할 수 있다.
- [프로그래머스 - 타겟 넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165): DFS와 재귀로 `+`, `-` 선택의 모든 경우를 탐색한다.
- [프로그래머스 - 단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163): 단어를 바꾸는 경로를 DFS 방식으로 탐색할 수 있다.
