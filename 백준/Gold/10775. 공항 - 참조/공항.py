# 처음 풀이 - 처음엔 docking 리스트를 만들어서 들어온 순서에 맞게 뒤로 보내서 채워주려고 하였으나
# 반례 -> 게이트: 4, 비행기: 4, 4-3-4-3 순으로 올떄 4-3-4-3 하고 끝나 4개가 나와야하는데 내 로직은 4-3-4 으로 끝나 3개가 나옴 - 내 풀이는 뒤에 여분의 추가 게이트가 있는 지 모름
import sys

input = sys.stdin.readline

G = int(input())
P = int(input())
airplanes = [int(input()) for _ in range(P)]    

count=0
docking = [0]*(G+1)
docking[0]=10001
for idx, airplane in enumerate(airplanes):
    if docking[airplane] == 0:
        count+=1
        docking[airplane] = idx+1
    else:
        if docking[airplane-docking[airplane]] == 0:
            count+=1
            docking[airplane-docking[airplane]] = docking[airplane]
            docking[airplane] = idx+1
        else:
            break

print(count)

# 뒤에 여분에 추가 게이트가 있는지 판단하기 위해 Find-Union 알고리즘을 사용해 각 게이트의 부모 게이트를 만들어 
# 현재 번호 게이트가 도킹되어 있으면 옆에 부모 게이트를 확인하여 비어있는 부모 게이트로 연결시키는 방식
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
