import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        
        int[] firstPattern = {1,2,3,4,5};
        int[] secondPattern = {2,1,2,3,2,4,2,5};
        int[] thirdPattern = {3,3,1,1,2,2,4,4,5,5};
        
        int[] counts = {0,0,0};
        
        for (int i=0; i<answers.length; i++) {
            if (answers[i] == firstPattern[i%firstPattern.length]) {
                counts[0]++;
            }
            if (answers[i] == secondPattern[i%secondPattern.length]) {
                counts[1]++;
            }
            if (answers[i] == thirdPattern[i%thirdPattern.length]) {
                counts[2]++;
            }
        }
        
        List<Integer> list = new ArrayList<>();
        int max = Arrays.stream(counts).max().orElse(0);
        
        for (int i=0; i<counts.length; i++) {
            if (counts[i] == max) {
                list.add(i+1);
            }
        }
        
        
        return list.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}