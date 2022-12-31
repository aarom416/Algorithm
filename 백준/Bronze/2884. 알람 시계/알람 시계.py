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

# 다른 풀이

H, M = map(int, input().split())
timer = int(input()) 

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)
