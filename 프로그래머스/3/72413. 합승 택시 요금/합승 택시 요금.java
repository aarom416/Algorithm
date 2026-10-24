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