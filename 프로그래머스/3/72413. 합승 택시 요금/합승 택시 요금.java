// 시간 복잡도를 줄이기 위해 매번 함수를 실행하는게 아니라 각 도착 시간에서 모든 지점까지의 최소 비용 거리 배열을 미리 다 구해놓고
// 합승 지점에서 모든 출발지점까지의 합으로 생각 전환 함수 3번이면 끝
// 기존 s -> i -> a,b => 출발지점 -> 합승지점(임의) -> a도착지점, b도착지점
// 변경 i -> s,a,b  => 합승지점(임의) -> 출발지점, a도착지점, b도착지점
import java.util.*;

class Solution {
    
    private static final int INF = Integer.MAX_VALUE;
    
    public int solution(int n, int s, int a, int b, int[][] fares) {

        int answer = INF;
        
        // i 를 합승지점으로 했을때 합승 지점으로부터 S,A,B 까지의 거리합 중 최소 => 해당 합승지점으로 했을때 가장 짧은 비용
        // 미리 S,A,B 에서 모든 최송 비용을 구하기
        int[] disS = dijkstra(n, s, fares);
        int[] disA = dijkstra(n, a, fares);
        int[] disB = dijkstra(n, b, fares);
        for (int i=1; i<=n; i++) {
            // s->i or a->i or b->i 지나갈 수 없는 경우
            if (disS[i] == INF || disA[i] == INF || disB[i] == INF) continue;
            
            answer = Math.min(answer, disS[i] + disA[i] + disB[i]);
        }
        
        return answer;
    }
    
    // 시작 지점에서 모든 최소 비용을 나타내는 배열
    public int[] dijkstra(int n, int start, int[][] fares) {
        
        boolean[] visited = new boolean[n+1];
        int[][] graph = new int[n+1][n+1];
        int[] distance = new int[n+1];
        
        // INF 처리
        for (int i=1; i<=n; i++) {
            Arrays.fill(graph[i], INF);
        }
        
        // 지점 정보 등록
        for (int[] f : fares) {
            graph[f[0]][f[1]] = f[2];
            graph[f[1]][f[0]] = f[2];
            // 본인 지점은 0
            graph[f[0]][f[0]] = 0;
        }
        
        // 비용 정보 등록
        Arrays.fill(distance, INF);
        distance[start] = 0;
        
        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.offer(new Node(start, 0));
        
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            int current = node.target;
            
            if (visited[current]) continue;
            
            visited[current] = true;
            
            for (int next=1; next<=n; next++) {
                // 인접X
                if (graph[current][next] == INF) continue;
                
                // 현재 지점까지 비용 + 다음 지점까지 비용
                int newCost = node.cost + graph[current][next];
                
                // 새 거리가 기존 최소 거리 보다 작은 경우 교체
                if (newCost < distance[next]) {
                    distance[next] = newCost;
                    queue.offer(new Node(next, newCost));
                }
            }
        }
        
        return distance;
    }
    
    
    class Node implements Comparable<Node> {
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

// 처음 풀이 - 답은 맞으나 n 이 커질수록 함수를 매번 3번씩 실행하며 시간 초과
import java.util.*;

class Solution {
    
    private static final int INF = Integer.MAX_VALUE;
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = INF;
        // 출발 지점 -> 합승 지점
        // 합승 지점 -> A 도착 지점
        // 합승 지점 -> B 도착 지점
        for (int i=1; i<=n; i++) {
            answer = Math.min(answer, dijkstra(n,s,i,fares)+dijkstra(n,i,a,fares)+dijkstra(n,i,b,fares));
        }
        return answer;
    }
    
    public int dijkstra(int n, int start, int end, int[][] fares) {
        
        boolean[] visited = new boolean[n+1];
        int[][] graph = new int[n+1][n+1];
        int[] distance = new int[n+1];
        
        // INF 처리
        for (int i=1; i<=n; i++) {
            Arrays.fill(graph[i], INF);
        }
        
        // 지점 정보 등록
        for (int[] f : fares) {
            graph[f[0]][f[1]] = f[2];
            graph[f[1]][f[0]] = f[2];
            // 본인 지점은 0
            graph[f[0]][f[0]] = 0;
        }
        
        // 비용 정보 등록
        Arrays.fill(distance, INF);
        distance[start] = 0;
        
        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.offer(new Node(start, 0));
        
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            int current = node.target;
            
            if (visited[current]) continue;
            
            visited[current] = true;
            
            for (int next=1; next<=n; next++) {
                // 인접X
                if (graph[current][next] == INF) continue;
                
                // 현재 지점까지 비용 + 다음 지점까지 비용
                int newCost = node.cost + graph[current][next];
                
                // 새 거리가 기존 최소 거리 보다 작은 경우 교체
                if (newCost < distance[next]) {
                    distance[next] = newCost;
                    queue.offer(new Node(next, newCost));
                }
            }
        }
        
        // 도착 지점까지의 최소값
        return distance[end];
    }
    
    
    class Node implements Comparable<Node> {
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
