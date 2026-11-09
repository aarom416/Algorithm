import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        for (int i=0; i<=discount.length-10; i++) {
            
            HashMap<String, Integer> map = new HashMap<>();
            
            for (int k=0; k<want.length; k++) {
                map.put(want[k], number[k]);
            }
            
            for (int j=0; j<10; j++) {
                String product = discount[i+j];
                
                if (map.containsKey(product)) {
                    map.put(product, map.get(product)-1);
                }
            }
            
            boolean possible = true;
            
            for (int count : map.values()) {
                if (count != 0) {
                    possible = false;
                    break;
                }
            }
            
            if (possible) {
                answer++;
            }
        }
        return answer;
    }
}