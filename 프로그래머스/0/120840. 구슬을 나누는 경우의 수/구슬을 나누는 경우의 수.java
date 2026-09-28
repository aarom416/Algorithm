class Solution {
    public int solution(int balls, int share) {
    
        return nCr(balls, share);
    }
    
    private int nCr(int n, int r) {
        
        if (r==0 || n==r) {
            return 1;
        }
        
        return nCr(n-1, r-1) + nCr(n-1, r);
    }
}