import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> answer = new ArrayList<>();
        
        for (int i=2; i<Math.sqrt(n)+1; i++) {
            if (n%i == 0) {
                answer.add(i);
            }
            
            while (n%i == 0) {
                n /= i;
            }
        }
        
        if (n>1) {
            answer.add(n);
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}