// 다익스트라 풀이
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

// 플로이드 워셜 풀이
import java.util.*;

class Solution {
    
    private static final int INF = 1000000000;
    
    public int solution(int n, int s, int a, int b, int[][] fares) {

        int answer = INF;
        
        int[][] dp = new int[n+1][n+1];
        
        // 정보 초기화
        for (int i=1; i<=n; i++) {
            Arrays.fill(dp[i], INF);
            dp[i][i] = 0;
        }
        for (int[] f : fares) {
            dp[f[0]][f[1]] = f[2];
            dp[f[1]][f[0]] = f[2];
        }
        
        for (int k=1; k<=n; k++) {
            for (int i=1; i<=n; i++) {
                for (int j=1; j<=n; j++) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j]);
                }
            }
        }
        
        // DP 이므로 인접해있지 않은 경로가 있다면 INF 값이 남아있을 수 있음 ex) case 2 번경우
        for (int i=1; i<=n; i++) {
            if (dp[i][s] == INF || dp[i][a] == INF || dp[i][b] == INF) continue;
            answer = Math.min(answer , dp[i][s] + dp[i][a] + dp[i][b]);
        }
        
        return answer;
    }
}
