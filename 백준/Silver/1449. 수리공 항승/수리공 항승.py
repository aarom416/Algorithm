import sys
input=sys.stdin.readline
n,l=map(int,input().split())
location=list(map(int,input().split()))
location.sort()
max_location=location[-1]
check=[True]*(max_location+l+1)
cnt=0
flag=False
for i in location:
    check[i]=False
for i in location:
    if check[i]:
        continue
    for j in range(i,i+l):
        if not check[j]:
            check[j]=True
            flag=True
    if flag:
        cnt+=1
        flag=False
print(cnt)        