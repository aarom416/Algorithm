import sys

H,M = map(int,sys.stdin.readline().split())
N = int(sys.stdin.readline())

if M+N>=60:
    if H+((M+N)//60)>=24:
        H-=24
    H = H+(M+N)//60
    print(f"{H} {(M+N)%60}")

else:
    print(f"{H} {(M+N)}")
