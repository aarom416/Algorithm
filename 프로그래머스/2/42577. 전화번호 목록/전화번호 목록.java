import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        Map<String, Integer> map = new HashMap<>();
        
        for (String p: phone_book) {
            map.put(p, map.getOrDefault(p,0)+1);    
        }
        
        
        for (String p : phone_book) {
            String temp = "";
            for (char c: p.toCharArray()) {
                temp += c;
                if (map.containsKey(temp) && !temp.equals(p)) {
                    return false;
                }
            }
            
        }
        return true;
    }
}