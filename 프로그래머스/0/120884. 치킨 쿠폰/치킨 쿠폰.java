class Solution {
    public int solution(int chicken) {
        
        int service = 0;
        int rest = 0;
        int total = 0;
        while (chicken >= 10) {
            service = chicken / 10;
            rest = chicken % 10 + service;
            total += service;
            chicken = rest;
        }
        return total;
    }
}