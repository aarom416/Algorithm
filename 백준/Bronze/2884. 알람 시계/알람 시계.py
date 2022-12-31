import sys

H,M = map(int,sys.stdin.readline().split())

if H>0 and M-45<0:
    H = H-1
    M = M+15 # M+60-45
    print(f"{H} {M}")
elif H==0 and M-45<0:
    H = H+23
    M = M+15 # M+60-45
    print(f"{H} {M}")
else :
    M = M-45
    print(f"{H} {M}")
