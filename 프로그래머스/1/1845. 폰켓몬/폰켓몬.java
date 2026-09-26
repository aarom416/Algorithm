import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int n: nums) {
            map.put(n, map.getOrDefault(n,1));
        }
        
        return Math.min(map.size(), nums.length/2);
    }
}