import java.util.*;

class Solution {
    public int[] solution(int[][] score) {
        
        List<Integer> sum = new ArrayList<>();
        
        for (int[] s: score) {
            sum.add(s[0] + s[1]);
        }
        
        List<Integer> sortedSum = new ArrayList<>(sum);
        
        sortedSum.sort(Collections.reverseOrder());
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i=0; i<sortedSum.size(); i++) {
            if (!map.containsKey(sortedSum.get(i))) {
                map.put(sortedSum.get(i), i+1);
            }
        }
        
        int[] numbers = new int[score.length];
        
        for (int i=0; i<score.length; i++) {
            numbers[i] = map.get(sum.get(i));
        }
        
        return numbers;
    }
}