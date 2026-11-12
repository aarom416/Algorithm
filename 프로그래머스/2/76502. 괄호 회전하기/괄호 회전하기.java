import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        Deque<Character> deque = new LinkedList<>();
        
        for (char c : s.toCharArray()) {
            deque.addLast(c);
        }
        
        for (int i=0; i<s.length(); i++) {
            deque.addLast(deque.pollFirst());
            
            if (check(new LinkedList<>(deque))) {
                answer++;
            }
        }
        return answer;
    }
    
    public boolean check(Deque<Character> d) {
        Stack<Character> stack = new Stack<>();
        
        while (!d.isEmpty()) {
            char c = d.pollLast();
            
            switch (c) {
                case '}':
                    stack.push(c);
                    break;
                case ']':
                    stack.push(c);
                    break;
                case ')':
                    stack.push(c);
                    break;
                case '{':
                    if (!stack.isEmpty() && stack.peek() == '}') {
                        stack.pop();
                    } else {
                        stack.push(c);
                    }
                    break;
                case '[':
                    if (!stack.isEmpty() && stack.peek() == ']') {
                        stack.pop();
                    } else {
                        stack.push(c);
                    }
                    break;
                case '(':
                    if (!stack.isEmpty() && stack.peek() == ')') {
                        stack.pop();
                    } else {
                        stack.push(c);
                    }
                    break;
            }
        }
        
        if (stack.isEmpty()) {
            return true;
        } else {
            return false;
        }
    }
}