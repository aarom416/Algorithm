import java.util.*;

class Solution {
    
    HashSet<List<Integer>> set = new HashSet<>();
    
    public int solution(String dirs) {
        int answer = 0;
            
        int currentX = 0;
        int currentY = 0;
        set.add(Arrays.asList(0,0));
        
        for (char d : dirs.toCharArray()) {
            
            int startX = currentX;
            int startY = currentY;
            
            switch (d) {
                case 'L':
                    currentX--;
                    break;
                case 'R':
                    currentX++;
                    break;
                case 'U':
                    currentY++;
                    break;
                case 'D':
                    currentY--;
                    break;
            }
            
            if (currentX > 5 || currentX < -5 || currentY > 5 || currentY < -5) {
                currentX = startX;
                currentY = startY;
                continue;
            }
            
            List<Integer> path = Arrays.asList(startX, startY, currentX, currentY);
            
            if (set.contains(path)) {
                continue;
            }
            
            // 정방향
            set.add(path);

            // 역방향
            set.add(Arrays.asList(currentX, currentY, startX, startY));
            
            answer++;
        }
        return answer;
    }
    
    
}