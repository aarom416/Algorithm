import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        
        int[] students = new int[n+2];
        
        Arrays.fill(students, 1);
        
        for (int r : reserve) students[r] ++;
        for (int l : lost) students[l] --;
        
        Arrays.sort(lost);
        
        for (int l : lost) {
            if (students[l] == 0) {
                if (students[l-1] > 1) {
                    students[l-1] --;
                    students[l] ++;
                } else if (students[l+1] > 1) {
                    students[l+1] --;
                    students[l] ++;
                }
            }
        }
        
        for (int i=1; i<n+1; i++) {
            if (students[i] > 0) answer++;
        }
        return answer;
    }
}