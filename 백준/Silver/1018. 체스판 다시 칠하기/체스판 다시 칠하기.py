import sys
m,n = map(int,sys.stdin.readline().split())
chess_board = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
a=[]
for p in range(m-7): #행 이동함에 따라
    for q in range(n-7): #열 이동함에 따라
        idx1=0 #W로 시작할 경우 바꿔야할 체스 판 개수
        idx2=0 #B로 시작할 경우 바꿔야할 체스 판 개수
        for i in range(p,p+8): #8*8 바둑판 개수 체크
            for j in range(q,q+8):
                if(i+j)%2==0:
                    if chess_board[i][j]!='W': #W로 시작한 경우
                        idx1+=1
                    if chess_board[i][j]!='B': #B로 시작한 경우
                        idx2+=1
                else:
                    if chess_board[i][j]!='B': #W로 시작한 경우
                        idx1+=1
                    if chess_board[i][j]!='W': #B로 시작한 경우
                        idx2+=1
        a.append(min(idx1,idx2))
print(min(a))