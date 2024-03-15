# import sys

# input = sys.stdin.readline

# G = int(input())
# P = int(input())
# airplanes = [int(input()) for _ in range(P)]    

# count=0
# docking = [0]*(G+1)
# docking[0]=10001
# for idx, airplane in enumerate(airplanes):
#     if docking[airplane] == 0:
#         count+=1
#         docking[airplane] = idx+1
#     else:
#         if docking[airplane-docking[airplane]] == 0:
#             count+=1
#             docking[airplane-docking[airplane]] = docking[airplane]
#             docking[airplane] = idx+1
#         else:
#             break

# print(count)

import sys

input = sys.stdin.readline

G = int(input())
P = int(input())
airplanes = [int(input()) for _ in range(P)]    
parents = [i for i in range(G+1)]
count=0
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parents[y] = x
    else:
        parents[x] = y

for plane in airplanes:
    x = find(plane) #현재 제일 끝에 있는(부모 노드) 게이트 찾기
    if x == 0: #바로 옆에 빈 게이트가 0이면 종료
        break
    union(x,x-1) # 바로 옆에 있는 빈 게이트와 연결해주는 로직 - 다음 비행기가 들어오면 빈 게이트에 배분하기 위해
    count+=1

print(count)