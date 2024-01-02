import sys
import collections

input = sys.stdin.readline

n = int(input())
buildings = list(map(int, input().split()))
answer=0

def cal_gradient(x1,y1,x2,y2): #기울기 구하는 함수
    return (y2-y1)/(x2-x1)

for idx, height in enumerate(buildings):
    left_max=float('inf')
    right_max=-float('inf')
    result=0
    for i in range(idx-1,-1,-1): #왼쪽 부분
        gradient = cal_gradient(idx+1,height,i+1,buildings[i])
        if left_max > gradient: #왼쪽 부분은 현재 최대 기울기보다 더 작아야 빌딩이 보임
            result+=1
            left_max=gradient
    
    for i in range(idx+1,n): #오른쪽 부분
        gradient = cal_gradient(idx+1,height,i+1,buildings[i])
        if right_max < gradient: #오른쪽 부분은 현재 최대 기울기보다 더 커야 빌딩이 보임
            result+=1
            right_max=gradient
    
    answer=max(answer,result) #최대값으로 갱신 
print(answer)
