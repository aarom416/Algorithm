import sys, heapq

input = sys.stdin.readline

n = int(input())
cranes = list(map(int,input().split()))
m = int(input())
boxes = list(map(int,input().split()))

cranes.sort(reverse=True) #가장 큰 크레인부터 처리를 위해 내림차순 정렬
boxes.sort(reverse=True) #가장 큰 박스부터 처리를 위해 내림차순 정렬

if cranes[0] < boxes[0]: #제일 큰 거끼리 비교했을때 박스가 더 크면 크레인 사용 못함
    print(-1)
    exit()
count=0
while boxes:
    for crane in cranes:
        #제일 작은 박스가 현재 크레인보다 크면 시간 절약을 위해 continue ex) cranes : 9,8,7 boxes : 9,9,9,9,9,9 8크기 크레인은 어짜피 못옮김 
        if boxes and crane < boxes[-1]: 
            continue
        for box in boxes:
            if crane>=box:
                boxes.remove(box) # remove 사용해 현재 위치 제거
                break
    count+=1
print(count)