import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
graph = [[[] for _ in range(n)] for _ in range(n)]
fireballs = []

for _ in range(m):
    #파이어볼 위치 정보 확인
    r,c,m,s,d = map(int,input().split())
    #r-1, c-1를 하여 인덱스 0으로 간편하게 처리할 수 있도록 함
    fireballs.append([r-1,c-1,m,s,d])

for _ in range(k):
    #파이어볼 이동
    while fireballs:
        now_r, now_c, now_m, now_s, now_d = fireballs.pop()
        #n으로 나눈 나머지를 하는 이유는 1번-N번행이 연결되어있음
        move_r = (now_r+now_s*dx[now_d])%n
        move_c = (now_c+now_s*dy[now_d])%n
        graph[move_r][move_c].append([now_m,now_s,now_d])
    
    for r in range(n):
        for c in range(n):
            #파이어볼 2개 이상인 경우 4개로 쪼개야함
            if len(graph[r][c]) > 1:
                sum_m, sum_s, count_odd, count_even, count = 0,0,0,0,len(graph[r][c])
                #현재 위치에 대한 파이어볼의 정보를 통해 각 정보를 처리
                while graph[r][c]:
                    cur_m,cur_s,cur_d = graph[r][c].pop()
                    sum_m+=cur_m
                    sum_s+=cur_s
                    if cur_d%2==0:
                        count_even += 1
                    else: 
                        count_odd += 1
                #방향 고정
                if count_even == count or count_odd == count:
                    direction = [0,2,4,6]
                else:
                    direction = [1,3,5,7]
                #질량이 0이면 소멸
                if sum_m//5:
                    #4개 방향에 대한 파이어볼 정보 삽입
                    for d in direction:
                        fireballs.append([r,c,sum_m//5, sum_s//count, d])
            #1개인 경우
            if len(graph[r][c]) == 1:
                fireballs.append([r,c]+graph[r][c].pop())
print(sum(fireball[2] for fireball in fireballs))