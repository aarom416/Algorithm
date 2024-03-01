import sys 
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int,input().split()))
if len(sensor)==1:
    print(0)
    exit()
# 센서 6, 집중국 2 sensor = 1 6 9 3 6 7 인 경우 
#원점에서 시작하므로 오름차순 정렬
#sensor = 1 3 6 6 7 9
sensor.sort()
dist = []
#각 센서 간에 거리 차이 dist = 2 3 0 1 2
for i in range(1,len(sensor)):
    dist.append(sensor[i]-sensor[i-1])
#센서 간 거리 가장 큰 센서를 제외 하기 위해 오름차순 정렬 dist = 0 1 2 2 3
dist.sort()
#6개 센서 중에 2개의 집중국으로 묶으러면 2개의 집중국을 잇는 센서 2개를 제외한 4개의 센서간 거리만 모두 더하면 됨 6-2 (n-k)
print(sum(dist[:n-k])) 