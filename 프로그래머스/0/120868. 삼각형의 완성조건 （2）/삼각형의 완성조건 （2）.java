import java.util.*;

class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        
        int min = Math.min(sides[0], sides[1]);
        
        answer = min + (min-1);
        return answer;
    }
}