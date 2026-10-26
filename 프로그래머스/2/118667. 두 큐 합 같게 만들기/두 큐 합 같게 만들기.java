import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int count = 0;
        
        Queue<Integer> q1 = new ArrayDeque<>();
        Queue<Integer> q2 = new ArrayDeque<>();
        
        // 1<=queue1,2 의 원소 <= 10^9 
        // 10^9 * 300,000 일 수 있으므로 int 값이 초과될 수 있으므로 long 타입 선언
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
        
        // 하나의 큐에서 돌고 다시 돌아올 수 있으므로 * 2
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