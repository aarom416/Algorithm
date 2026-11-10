import java.util.*;

class Solution {
    int answer = 0;
    int count = 0;
    String target;
    
    String[] values = {"A", "E", "I", "O", "U"};
    
    public int solution(String word) {
        target = word;
        dfs("");
        return answer;
    }
    
    public void dfs(String current) {
        if (current.length() > 5) {
            return;
        }
        
        if (!current.isEmpty()) {
            count++;
            
            if (current.equals(target)) {
                answer = count;
            }
        }
        
        for (int i=0; i<5; i++) {
            dfs(current + values[i]);
        }
    }
}