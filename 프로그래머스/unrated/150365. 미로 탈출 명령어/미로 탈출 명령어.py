import sys
sys.setrecursionlimit(10**6)
dx=[1,0,0,-1]
dy=[0,-1,1,0]
string=['d','l','r','u']
answer='z'
def valid(n,m,nx,ny):
    if 1<=nx<=n and 1<=ny<=m:
        return True
    else:
        return False
    
def dfs(n,m,x,y,r,c,prev_string,count,k):
    global answer
    if k<count+abs(r-x)+abs(c-y):
        return
    if x==r and y==c and count==k:
        answer=prev_string
        return
    for i in range(4):
        if valid(n,m,x+dx[i],y+dy[i]) and prev_string<answer:
            dfs(n,m,x+dx[i],y+dy[i],r,c,prev_string+string[i],count+1,k)
def solution(n, m, x, y, r, c, k):
    distance=abs(r-x)+abs(c-y)
    if distance>k or (distance-k)%2==1:
        return 'impossible'
    dfs(n,m,x,y,r,c,'',0,k)
    return answer
    