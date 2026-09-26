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