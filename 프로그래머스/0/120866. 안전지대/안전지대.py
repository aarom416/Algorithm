def solution(board):
    n = len(board)         
    m = len(board[0])       
    
    bombs = []
    for i in range(n):
        for j, b in enumerate(board[i]):
            if b == 1:
                bombs.append([i,j])
                
    for i, j in bombs:
        
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ni = i + di
                nj = j + dj
                
                if 0 <= ni < n and 0 <= nj < m:
                    board[ni][nj] += 1
        
    answer = 0
    for i in range(n):
        for j, b in enumerate(board[i]):
            if b == 0:
                answer += 1
        
    return answer