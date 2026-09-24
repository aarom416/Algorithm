class Solution {
    public int solution(int n) {
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            count += 1;
            while (count % 3 == 0 || String.valueOf(count).contains("3")) {
                count+=1;
            }
        }
        return count;
    }
}