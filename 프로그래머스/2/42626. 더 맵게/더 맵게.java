import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        
        for (int s: scoville) {
            queue.offer(s);
        }
        
        while (!queue.isEmpty()) {
            
            if (queue.peek() >= K) {
                return answer;
            }
            
            if (queue.size() < 2) {
                return -1;
            }
            
            int mix = queue.poll() + queue.poll() * 2;
            
            queue.offer(mix);
            answer++;
                
        }
        
        return -1;
    }
}