import java.util.*;

class Solution {
    public int solution(int[] array) {
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int num: array) {
            map.put(num, map.getOrDefault(num, 0) +1);
        }
        
        int maxCount = 0;
        int answer = 0;
        for (int key: map.keySet()) {
            int count = map.get(key);
            
            if (count > maxCount) {
                maxCount = count;
                answer = key;
            } else if (maxCount == count) {
                answer = -1;
            }
        }
        
        return answer;
    }
}