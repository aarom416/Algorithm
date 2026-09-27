import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        String[] answers = Arrays.stream(numbers)
            .mapToObj(String::valueOf)
            .sorted((a,b) -> (b+a).compareTo(a+b))
            .toArray(String[]::new);
        
        if (answers[0].equals("0")) {
            return "0";
        }
        
        return String.join("", answers);
    }
}