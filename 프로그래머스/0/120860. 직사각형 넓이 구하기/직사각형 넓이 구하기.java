import java.util.*;

class Solution {
    public int solution(int[][] dots) {
        int answer = 0;
        
        Arrays.sort(dots, (a,b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
            
        });
        
        int y = dots[1][1] - dots[0][1];
        int x = dots[2][0] - dots[0][0];
        
        return x*y;
    }
}