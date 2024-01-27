#풀이참조
import sys  
sys.setrecursionlimit(10**6)
dx=[1,0,0,-1]
dy=[0,-1,1,0]
string=['d','l','r','u']
answer='z' #파이썬은 문자열 제일 앞에 있는 문자를 기준으로 하나씩 비교하기 때문에 제일 큰 z를 두어 처음에 prev_string 값에 문자가 채워질 수 있게 함
def valid(n,m,nx,ny): #현재 위치가 유효한지 확인(밖으로 나간건지 확인)
    if 1<=nx<=n and 1<=ny<=m:
        return True
    else:
        return False
def dfs(n,m,x,y,r,c,prev_string,count,k): #dfs를 통해 순서가 작은 d,l,r,u 순으로 탐색
    global answer
    if k<count+abs(r-x)+abs(c-y): #횟수안에 못들어온 경우
        return
    if x==r and y==c and count==k: #도착 지점에 온 경우 
        answer=prev_string #사전 순이 가장 빠른 것을 찾기 위해 answer에 저장
        return
    for i in range(4):
        if valid(n,m,x+dx[i],y+dy[i]) and prev_string<answer: #벽 안에 있고 answer 값과 비교하며 사전 순으로 가장 빠른 명령어 찾음
            dfs(n,m,x+dx[i],y+dy[i],r,c,prev_string+string[i],count+1,k)
def solution(n, m, x, y, r, c, k):
    distance=abs(r-x)+abs(c-y)
    if distance>k or (distance-k)%2==1: #k횟수안에 못들어오거나 최소 거리로 도착후 이동할 수 있는 횟수가 홀수인 경우 불가능
        return 'impossible'
    dfs(n,m,x,y,r,c,'',0,k)
    return answer

#9.2점/100점
#dfs를 떠올렸으나 d,l,r,u 순으로 확인해야된다는 점과 움직일때마다 움직인 방향에 따른 문자열 추가 방법이 떠올리지 않았음
#각 로직에 따른 함수를 만들어 가독성과 간단성을 잘 적용시킨 코드를 짜는 연습이 필요한거 같음
def solution(n, m, x, y, r, c, k):
    answer = ''
    answer_list=[]
    a=r-x
    b=c-y
    if a>0:
        answer+='d'*a
    elif a<0:
        answer+='u'*abs(a)
    if b>0:
        answer+='r'*b
    elif b<0:
        answer+='l'*abs(b)
    answer=''.join(sorted(answer))
    ud_answer=answer[:]
    lr_answer=answer[:]
    k=k-(abs(a)+abs(b))
    if k%2==0:
        ud_cnt=k
        lr_cnt=k
        ud_count=n-r
        lr_count=m-c
        for _ in range(k):
            if k>=4 and ud_cnt==(k//2):
                ud_answer+='u'*ud_cnt
                break
            if ud_count>0:
                ud_answer+='d'
                ud_count-=1
                ud_cnt-=1
            else:
                ud_answer+='u'
                ud_count+=1
                ud_cnt-=1
        answer_list.append(ud_answer)
                           
        for _ in range(k):
            if k>=4 and lr_cnt==(k//2):
                lr_answer+='r'*lr_cnt
                break
            if c>1:
                lr_answer+='l'
                c-=1
                lr_cnt-=1
            else:
                lr_answer+='r'
                c+=1
                lr_cnt-=1
        answer_list.append(lr_answer)
        return min(answer_list)
    else:
        return "impossible"
    
