import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        
        int INF = Integer.MAX_VALUE;
        
        int[][] graph = new int[N+1][N+1];
        int[] distance = new int[N+1];
        boolean[] visited = new boolean[N+1];
        
        // INF 초기화
        for (int i=1; i<=N; i++) {
            Arrays.fill(graph[i], INF);
        }
        
        // 배달 정보 입력 - 양방향(중요)
        for (int[] r : road) {
            int from = r[0];
            int to = r[1];
            int cost = r[2];
            graph[from][to] = Math.min(cost, graph[from][to]);
            graph[to][from] = Math.min(cost, graph[to][from]);
        }
        for (int i=1; i<=N; i++) {
            graph[i][i] = 0; // 자기 자신은 거리 0
        }
        
        // 거리 정보 초기화
        Arrays.fill(distance, INF);
        
        // 1부터 시작을 위해 
        distance[1] = 0;
        
        // 우선순위큐에 시작1 에 대한 Node(목표 지점, 비용) 저장
        // 정렬 기준은 반드시 필요 -> 최소힙이기 때문에 각 노드의 비용을 비교 최대힙인 경우, (b.cost, a.cost)
        PriorityQueue<Node> queue = new PriorityQueue<>((a,b ) -> Integer.compare(a.cost, b.cost));
        queue.offer(new Node(1,0));
        
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            int current = node.target;
            
            visited[node.target] = true;
            
            // 인접 배달 지역 탐색
            for (int next=1; next<=N; next++) {
                // 연결X
                if (graph[current][next] == INF) {
                    continue;
                }
                
                // 현재 배달지역까지의 비용 + 다음 배달 지역까지의 비용
                int newCost = node.cost + graph[current][next];
                // 다음 배달지역의 최소 거리보다 신규 비용이 작은 경우 갱신
                if (newCost < distance[next]) {
                    distance[next] = newCost;
                    // 다음 배달 지역을 큐에 넣기
                    queue.offer(new Node(next, distance[next]));
                }
                
            } 
        }
        
        for (int d : distance) {
            if (d <= K) {
                answer++;
            }
        }
        return answer;
    }
    
    // 배달 정보를 저장할 노드 객체
    class Node {
        int target;
        int cost;
        
        Node(int target, int cost) {
            this.target = target;
            this.cost = cost;
        }
    }
}

// Node 클래스에서 Comparable 인터페이스를 구현하고 compareTo()를 오버라이딩
import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        
        int INF = Integer.MAX_VALUE;
        
        int[][] graph = new int[N+1][N+1];
        int[] distance = new int[N+1];
        boolean[] visited = new boolean[N+1];
        
        // INF 초기화
        for (int i=1; i<=N; i++) {
            Arrays.fill(graph[i], INF);
        }
        
        // 배달 정보 입력 - 양방향(중요)
        for (int[] r : road) {
            int from = r[0];
            int to = r[1];
            int cost = r[2];
            graph[from][to] = Math.min(cost, graph[from][to]);
            graph[to][from] = Math.min(cost, graph[to][from]);
        }
        for (int i=1; i<=N; i++) {
            graph[i][i] = 0; // 자기 자신은 거리 0
        }
        
        // 거리 정보 초기화
        Arrays.fill(distance, INF);
        
        // 1부터 시작을 위해 
        distance[1] = 0;
        
        // 우선순위큐에 시작1 에 대한 Node(목표 지점, 비용) 저장
        // 정렬 기준은 반드시 필요 -> 최소힙이기 때문에 각 노드의 비용을 비교 최대힙인 경우, (b.cost, a.cost)
        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.offer(new Node(1,0));
        
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            int current = node.target;
            
            visited[node.target] = true;
            
            // 인접 배달 지역 탐색
            for (int next=1; next<=N; next++) {
                // 연결X
                if (graph[current][next] == INF) {
                    continue;
                }
                
                // 현재 배달지역까지의 비용 + 다음 배달 지역까지의 비용
                int newCost = node.cost + graph[current][next];
                // 다음 배달지역의 최소 거리보다 신규 비용이 작은 경우 갱신
                if (newCost < distance[next]) {
                    distance[next] = newCost;
                    // 다음 배달 지역을 큐에 넣기
                    queue.offer(new Node(next, distance[next]));
                }
                
            } 
        }
        
        for (int d : distance) {
            if (d <= K) {
                answer++;
            }
        }
        return answer;
    }
    
    // 배달 정보를 저장할 노드 객체
    class Node implements Comparable<Node>{
        int target;
        int cost;
        
        public Node(int target, int cost) {
            this.target = target;
            this.cost = cost;
        }
        
        @Override
        public int compareTo(Node n) {
            if (this.cost > n.cost) {
                return 1;
            }
            return -1;
        }
    }
}
