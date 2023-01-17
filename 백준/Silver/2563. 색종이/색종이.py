n = int(input())

paper = [[0 for _ in range(100)] for _ in range(100)] #종이 넓이 초기화

for _ in range(n):
    x,y = map(int, input().split())
    for i in range(x,x+10): #x,y에서 10*10만큼 배열값 1로 선언
        for j in range(y,y+10):
            paper[i][j]= 1
cnt = 0
for i in paper: #리스트에서 1의 개수 카운트-> 넓이
    cnt += i.count(1)
print(cnt)
