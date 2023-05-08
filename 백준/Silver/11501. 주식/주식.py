import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n=int(input())
    stock=list(map(int,input().split()))
    max_stock=0
    result=0
    for i in range(len(stock)-1,-1,-1): 
        if max_stock<=stock[i]:
            max_stock=stock[i]
        else:
            result+=max_stock-stock[i]
    print(result)