import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        
        List<Integer> list = new ArrayList<>();
        
        for (int[] command: commands) {
            int[] copy = Arrays.copyOfRange(array, command[0]-1, command[1]);
            Arrays.sort(copy);
            list.add(copy[command[2]-1]);
        }
        
        return list.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}