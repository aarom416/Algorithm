import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

def binary_serach(start, end, target):
    while start<=end:
        mid = (start+end)//2 #특정수 mid 
        cnt = 0
        for i in range(1,n+1): #특정수 mid 보다 작은 수들이 총 몇 개인지 확인
            cnt += min(mid//i,n) #특정수를 1부터 나눠서 몇 개인지 각 몇 개인지 확인할때 n개를 넘으면 안됨
        if cnt >= target: #특정 수보다 작은 숫자의 개수가 k번째보다 큰 경우 -> k번째를 넘어간 것이므로 end를 내림
            end = mid - 1
        else:
            start = mid + 1 #특정 수보다 작은 숫자의 개수가 k번째보다 작은 경우 -> k번째 안에 있으모로 start를 올림
    return start
print(binary_serach(0,n*n,k))