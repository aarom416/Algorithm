import java.util.*;

class Solution {
    public int solution(int a, int b) {
        
        int m = Math.min(a,b);
        
        for (int i = m; i>=1; i--) {
            if (a%i==0 && b%i==0) {
                a /= i;
                b /= i;
                break;
            }
        }
        
//         b /= gcd;
        
        while (b%2==0) {
            b /= 2;
        }
        
        while (b%5==0) {
            b /= 5;
        }
        
        return (b == 1) ? 1 : 2;
    }
    
    // 유클리드 호제법
    private int getGcd(int a, int b) {
        if (b==0) {
            return a;
        }
        return getGcd(b, a%b);
    }
}