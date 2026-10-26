import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int count = 0;
        
        Queue<Integer> q1 = new ArrayDeque<>();
        Queue<Integer> q2 = new ArrayDeque<>();
        
        long totalQ1 = 0;
        long totalQ2 = 0;
        
        for (int q : queue1) {
            q1.offer(q);
            totalQ1 += q;
        }
        for (int q : queue2) {
            q2.offer(q);
            totalQ2 += q;
        }
        
        int limit = (queue1.length + queue2.length) * 2;
        
        // 각각 나눴을때 소숫점이 나오면 만들 수 없음
        if ((totalQ1 + totalQ2) % 2 != 0) {
            return -1;
        }
        
        while (totalQ1 != totalQ2) {
            
            if (count >= limit) {
                return -1;
            }
            
            if (totalQ1 > totalQ2) {
                int value = q1.poll();
                totalQ2 += value;
                totalQ1 -= value;
                q2.offer(value);
            } else {
                int value = q2.poll();
                totalQ1 += value;
                totalQ2 -= value;
                q1.offer(value);
            }
            
            count++;
        }
        
        return count;
    }
}