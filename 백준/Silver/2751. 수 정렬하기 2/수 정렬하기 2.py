import sys
n = int(input())
num = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
num.sort()
for i in num:
    print(i)