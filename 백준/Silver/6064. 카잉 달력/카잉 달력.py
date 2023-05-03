import sys
input=sys.stdin.readline
num=int(input())
for _ in range(num):
    m,n,x,y=map(int,input().split())
    k=x
    flag=False #k 값 찾았는지에 대한 변수 초기화
    while k<=m*n:
        # 10,12,3,9 인 경우 k=10*p+3=12*q+9 와 같음
        # x=3 이면 x 가 될 수 있는 수는 13,23,33...
        # y=9 이면 y 가 될 수 있는 수는 9,21,33...
        if (k-x)%m==0 and (k-y)%n==0: 
            print(k)
            flag=True #k 값 찾았으므로 True
            break
        k+=m
    if not flag:
        print(-1)