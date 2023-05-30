# 풀이 참조 - 우선순위 큐 사용
import sys
import heapq
input=sys.stdin.readline
n,k=map(int,input().split())
answer=0
jewel=[]
for _ in range(n):
    heapq.heappush(jewel,list(map(int,input().split()))) #최소힙을 사용해 각 가방에 넣을 수 있는 모든 보석 찾기
bags=[]
for _ in range(k):
    bags.append(int(input().rstrip()))
bags.sort()
tmp_jewel=[]
for bag in bags:
    while jewel and bag>=jewel[0][0]:
        heapq.heappush(tmp_jewel, -heapq.heappop(jewel)[1]) #최대힙을 사용해 각 가방에 넣을 수 있는 보석 중 가장 가치가 큰 보석 찾기
    if tmp_jewel:
        answer-=heapq.heappop(tmp_jewel)
    elif not jewel:
        break
print(answer)

# 나의 풀이 -> ex) 보석: (7,100) (100,7) 가방: 100,7 경우 내 풀이는 가방의 무게를 내림차순 정렬하기 때문에 무게가 7인 보석만 담아
# 최대 가치가 100이 된다. 하지만 보석의 무게가 100인 것은 가방의 무게가 100인 것을 사용하고 보석의 무게가 7인 것은 가방의 무게가 7
# 인 것을 사용해야 한다. 
# 너무 최대 가치를 기준으로만 본 것이 잘못된 생각 -> 최대 가치가 기준이 아닌거 같으면 두번째 요소인 무게를 기준으로 생각을 해볼 필요가 있었음

import sys
input=sys.stdin.readline
n,k=map(int,input().split())
jewel=[]
bag_weight=[]
answer=0
for _ in range(n):
    a,b=map(int,input().split())
    jewel.append((a,b))
for _ in range(k):
    bag_weight.append(int(input().rstrip()))
    
jewel.sort(key=lambda x:(x[1],x[0]), reverse=True)
bag_weight.sort(reverse=True)
bag_use=[False]*len(bag_weight)

for weight,value in jewel:
    weight_idx_stack=[]
    value_stack=[]
    for i in range(len(bag_weight)):
        if bag_weight[i]>weight:
            weight_idx_stack.append(i)
            value_stack.append(value)
        elif bag_weight[i]==weight:
            answer+=value
            bag_use[i]=True
            break
        elif bag_weight[i]<weight and weight_idx_stack:
            answer+=value_stack.pop()
            bag_use[weight_idx_stack.pop()]=True
            break
        else:
            break
print(answer)
