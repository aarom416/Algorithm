// 그리디 풀이
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

        // 모든 값이 같아질 떄까지 넣고 뺴고를 반복
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

// 투 포인터 풀이 
// 두개의 배열를 하나의 배열로 만들고 두개의 포인터를 이동해가면 합 비교
import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        
        int[] queue = new int[queue1.length + queue2.length];
        
        for (int i=0; i<queue1.length; i++) {
            queue[i] = queue1[i];
            queue[i+queue1.length] = queue2[i];
        }
        
        
        long sum1 = Arrays.stream(queue1).sum();
        long sum2 = Arrays.stream(queue2).sum();
        long mid = (sum1 + sum2) / 2;
        
        int left = 0;
        int right = queue1.length;
        int count = 0;
        
        // queue1를 다 사용할때까지 확인
        while (left<right) {
            // queue1의 합이 목표하는 mid 보다 작은 경우 -> queue2에서 보내줘야함
            // 이떄 right 가 제일 끝값에 위치할 수 있으므로 queue의 총 길이보다 작은지 체크,
            if (right < queue.length && sum1 < mid) {
                // queue2의 현재값을 보내 더해주고 right + 1
                sum1 += queue[right++];
            } else if (sum1 == mid) {
                return count;
            // queue1의 합이 목표하는 mid 보다 큰 경우 -> queue1에서 제거해줘야함
            } else {
                sum1 -= queue[left++];
            }
            
            count++;
        }
        return -1;
    }
}
