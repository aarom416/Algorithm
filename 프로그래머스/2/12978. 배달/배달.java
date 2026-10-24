import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        
        int[][] dp = new int[N+1][N+1];
        
        // 다익스트라와 다르게 DP 를 갱신하면서 진행하기 떄문에 INF + INF = -2 가 나올 수 있음
        // 따라서 적당히 큰 10억을 넣음
        int INF = 1000000000;
        
        // INF 초기화
        for (int i=1; i<=N; i++) {
            Arrays.fill(dp[i], INF);
        }
        
        // 자기 자신 거리 0
        for (int i=1; i<=N; i++) {
            dp[i][i] = 0;
        }
        
        // 도로 정보 저장
        for (int[] r : road) {
            int from = r[0];
            int to = r[1];
            int cost = r[2];
            
            dp[from][to] = Math.min(cost, dp[from][to]);
            dp[to][from] = Math.min(cost, dp[to][from]);
        }
        
        // i~j 까지의 거리와 i~k + k~j (k를 거쳐 j로) 가는 최소 비용 완전 탐색
        for (int k=1; k<=N; k++) {
            for (int i=1; i<=N; i++) {
                for (int j=1; j<=N; j++) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j]);
                }
            }
        }
        
        for (int i=1; i<=N; i++) {
            if (dp[1][i] <= K) {
                answer++;
            }
        }
        return answer;
    }
}