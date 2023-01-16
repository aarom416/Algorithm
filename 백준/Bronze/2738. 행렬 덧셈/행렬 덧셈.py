a,b = [],[]
n,m = map(int,input().split())

for row in range(n):
    row = list(map(int,input().split()))
    a.append(row)
for row in range(n):
    row = list(map(int,input().split()))
    b.append(row)

for row in range(n):
    for col in range(m):
        print(a[row][col]+b[row][col], end=" ")
    print()

# 다른 풀이

n,m = map(int,input().split())
a=[0 for _ in range(m) for _ in range(n)]
b=[0 for _ in range(m) for _ in range(n)]
for i in range(n):
        a[i] = list(map(int,input().split()))
for i in range(n):
        b[i] = list(map(int,input().split()))
for i in range(n):
    for j in range(m):
        a[i][j]+=b[i][j]
        print(a[i][j],end=" ")
    print()
