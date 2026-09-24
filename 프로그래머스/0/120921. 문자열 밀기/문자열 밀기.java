class Solution {
    public int solution(String A, String B) {
        
        if (A.equals(B)) {
            return 0;
        }
        
        int l = A.length();
        
        for (int i=1; i<l; i++) {
            A = A.substring(l-1) + A.substring(0, l-1);
            if (A.equals(B)) {
                return i;
            }
        }
        return -1;
    }
}