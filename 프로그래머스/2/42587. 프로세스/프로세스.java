import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Queue<Progress> queue = new LinkedList<>();
        
        for (int i=0; i<priorities.length; i++) {
            Progress progress = new Progress(i, priorities[i]);
            queue.offer(progress);
        }
        
        while (true) {
            Progress current = queue.poll();
            
            if (queue.stream().anyMatch(q -> q.priority > current.priority)) {
                queue.offer(current);
            } else {
                answer+=1;
                if (location == current.index) {
                    return answer;
                }
            }
        }
    }
    
    private class Progress {
        final int index;
        final int priority;
        
        public Progress(int index, int priority) {
            this.index = index;
            this.priority = priority;
        }
    }
}