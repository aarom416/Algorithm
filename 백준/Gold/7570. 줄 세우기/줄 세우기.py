#처음 풀이 - 부모 노드를 이용해서 스왑시켜 풀이하였으나 주어진 테스트케이스만 통과하고 다른 반례 때문에 실패
# import sys

# input = sys.stdin.readline

# n = int(input().rstrip())
# childrens = [0]+list(map(int,input().split()))

# sorted_childrens = [i for i in range(n+1)]
# count=0
# parents = [i for i in range(n+1)]

# def find(x):
#     if x != parents[x]:
#         parents[x] = find(parents[x])
#     return parents[x]

# def union(x,y):
#     x = find(x)
#     y = find(y)
#     if x<y:
#         parents[x] = y
#     else:
#         parents[y] = x
        
# while sorted_childrens != childrens:
#     for idx, children in enumerate(childrens):
#         if children == sorted_childrens[idx]:
#             continue
#         x = find(childrens[idx])
#         union(sorted_childrens[idx],x)
#         sorted_childrens[x] = sorted_childrens[idx]
#         sorted_childrens[idx] = childrens[idx]
#         count+=1
# print(count)

#오름차순으로 증가하는 부분들을 제외한 부분들을 움직이면 됨 - 최대 오름차순을 구해 전체 개수에서 빼면 됨
import sys

input = sys.stdin.readline

n = int(input().rstrip())

childrens = list(map(int,input().split()))
children_loc = [-1]*(n+1)
#인덱스를 통해 위치 확인
for idx, children in enumerate(childrens):
    children_loc[children] = idx 

count=1
result=0
#오름차순이 최대 얼마나 증가하는 지 확인
for i in range(1,n):
    if children_loc[i] < children_loc[i+1]:
        count+=1
        #현재 오름차순 저장하고 오름차순 초기화
    else:
        result = max(result,count)
        count=1

print(n-result if n != 1 else 0)
