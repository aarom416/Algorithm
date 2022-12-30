import sys

chess = [1,1,2,2,2,8]
a = list(map(int,sys.stdin.readline().split()))

for i in range(6) :
        print(f"{chess[i]-a[i]}",end=" ")