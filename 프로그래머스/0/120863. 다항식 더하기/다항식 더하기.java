class Solution {
    public String solution(String polynomial) {
        String answer = "";
        
        String[] terms = polynomial.split(" \\+ ");
        
        int xCount = 0;
        int count = 0;
        
        for (String t : terms) {
            if (t.contains("x")) {
                if (t.equals("x")) {
                    xCount += 1;
                } else {
                    xCount += Integer.parseInt(t.replace("x", ""));
                }
            } else {
                count += Integer.parseInt(t);
            }
        }
        
        String xStr = "";
        if (xCount == 1) {
            xStr = "x";
        } else {
            xStr = xCount + "x";
        }
        
        if (xCount > 0 && count > 0) {
            answer = xStr + " + " + count;
        } else if (xCount > 0 && count == 0) {
            answer = xStr;
        } else {
            answer = String.valueOf(count);
        }
        
        return answer;
    }
}