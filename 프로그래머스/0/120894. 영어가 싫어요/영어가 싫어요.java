class Solution {
    public long solution(String numbers) {
        long answer = 0;
        
        String[] words = {"zero","one","two","three","four","five","six","seven","eight","nine"};
        
        for (int i=0; i<words.length; i++) {
            numbers = numbers.replace(words[i], String.valueOf(i));
        }
        return Long.parseLong(numbers);
    }
}