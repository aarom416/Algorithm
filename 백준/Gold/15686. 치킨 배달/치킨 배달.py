import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]
house = []
chicken_house = []
#치킨집과 집 좌표 
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i,j))
        elif graph[i][j] == 2:
            chicken_house.append((i,j))   
result = 1e9
#combinations 모듈을 사용하여 치킨집을 뽑고 각 집에서 부터 m개의 치킨집까지 걸리는 거리의 최소값 갱신
for chicken in combinations(chicken_house,m):
    temp = 0 # 전체 치킨집에서 긱 m개 뽑았을때 치킨 거리의 최소를 갱신시켜줄 변수
    for h in house:
        dist = 1e9 #각 집에서 치킨집까지의 거리의 최소를 갱신시켜줄 변수
        for j in range(m):
            dist = min(dist, abs(chicken[j][0]-h[0])+abs(chicken[j][1]-h[1]))
        temp+=dist
    result = min(result, temp)
print(result)