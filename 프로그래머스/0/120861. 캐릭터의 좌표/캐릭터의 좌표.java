class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = {};
        
        int xMove = 0;
        int yMove = 0;
        
        int xLimit = (board[0]-1)/2;
        int yLimit = (board[1]-1)/2;
        
        for (String k: keyinput) {
            
            int newX = xMove;
            int newY = yMove;
            
            switch (k) {
                case "left":
                    newX -= 1;
                    break;
                case "right":
                    newX += 1;
                    break;
                case "up":
                    newY += 1;
                    break;
                case "down":
                    newY -= 1;
                    break;
            }
            
            if (newX >= -xLimit && newX <= xLimit) {
                xMove = newX;
            }
            if (newY >= -yLimit && newY <= yLimit) {
                yMove = newY;
            }
        }
        
        return new int[]{xMove, yMove};
    }
}