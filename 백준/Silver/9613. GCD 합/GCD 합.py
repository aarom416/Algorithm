import sys,math
import sys
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    num,num_list,gcd=a[0],a[1:],0
    for i in range(len(num_list)-1):
        for j in range(i+1,len(num_list)):
            gcd+=math.gcd(num_list[i],num_list[j]) #math 모듈의 gcd 함수 사용
    print(gcd)
