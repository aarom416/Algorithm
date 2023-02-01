t = int(input())
for _ in range(t):
    m,n=map(int,input().split())
    a,b=1,1
    for i in range(2,m+1):
        while m%i==0 and n%i==0:
            m=m//i
            n=n//i
            a*=i
    print(a*m*n)
