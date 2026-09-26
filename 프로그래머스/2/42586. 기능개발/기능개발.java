import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        Deque<Integer> lastDay = new ArrayDeque<>();
        
        for (int i=0; i<progresses.length; i++) {
            if ((100-progresses[i])%speeds[i]>0) {
                lastDay.addLast((100-progresses[i])/speeds[i] + 1);
            } else {
                lastDay.addLast((100-progresses[i])/speeds[i]);
            }
        }
        
        List<Integer> answers = new ArrayList<>();
            
        int maxDay = lastDay.pollFirst();
        int temp = 1;
        
        while (!lastDay.isEmpty()) {
            int nextDay = lastDay.pollFirst();
            
            if (maxDay < nextDay) {
                answers.add(temp);
                temp=1;
                maxDay = nextDay;
            } else {
                temp +=1;
            }
        }
        
        answers.add(temp);
        
        return answers.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}

# 다른 풀이 - Queue 자료구조 이용
import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        Queue<Integer> q = new LinkedList<>();
        List<Integer> answerList = new ArrayList();
        
        for (int i=0; i<speeds.length; i++) {
            double last = (100-progresses[i])/ (double) speeds[i];
            int lastDay = (int) Math.ceil(last);
            
            if (!q.isEmpty() && q.peek() < lastDay) {
                answerList.add(q.size());
                q.clear();
            }
            
            q.offer(lastDay);
        }
        
        answerList.add(q.size());
        
        int[] answer = new int[answerList.size()];
        
        for (int i=0; i<answer.length; i++) {
            answer[i] = answerList.get(i);
        }
        
        return answer;
    }
}
