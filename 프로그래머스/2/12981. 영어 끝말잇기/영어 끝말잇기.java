import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {};

        Set<String> set = new HashSet<>();
        
        char lastWord = words[0].charAt(words[0].length()-1);
        set.add(words[0]);
        
        for (int i=1; i<words.length; i++) {
            
            if (words[i].charAt(0) == lastWord && !set.contains(words[i])) {
                lastWord = words[i].charAt(words[i].length()-1);
                set.add(words[i]);
                continue;
            }
            
            int number = i%n+1;
            int order = i/n+1;

            return new int[]{number, order};
        }
        return new int[]{0,0};
    }
}