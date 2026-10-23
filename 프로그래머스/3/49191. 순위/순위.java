class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        // know[a][b] = a가 b를 이겼음을 알고 있음
        boolean[][] know = new boolean[n+1][n+1];
        
        // 승패 정보 입력 - 단방향
        for (int[] result : results) {
            know[result[0]][result[1]] = true;
        }
        
        // i가 k를 이기고, k가 j를 이기면
        // i가 j를 이긴다는 것도 알 수 있음
        for (int k=1; k<=n; k++) {
            for (int i=1; i<=n; i++) {
                for (int j=1; j<=n; j++) {
                    if (know[i][k] && know[k][j]) know[i][j] = true;
                }
            }
        }
        
        // 자신을 제외한 모든 사람의 승패를 아는 경우 순위를 알 수 있음
        for (int i=1; i<=n; i++) {
            int count = 0;
            for (int j=1; j<=n; j++) {
                // i가 j를 이겼든, j가 i를 이겼든 하나만 알아도 승패 암
                if (know[i][j] || know[j][i]) count++;
            }
            if (count == n-1) {
                answer++;
            }
        }
        return answer;
    }
}