def solution(keyinput, board):
    answer = []
    
    x_move = 0
    y_move = 0
    
    x_limit = (board[0]-1)//2
    y_limit = (board[1]-1)//2
    
    for k in keyinput:
        
        new_x, new_y = x_move, y_move
        
        match k:
            case "left":
                new_x -=1
            case "right":
                new_x +=1
            case "up":
                new_y +=1
            case "down":
                new_y -=1
        
        if -x_limit <= new_x <= x_limit:
            x_move = new_x
        if -y_limit <= new_y <= y_limit:
            y_move = new_y
    return [x_move, y_move]