#시간 초과 -> 삼중 for 문은 1,000,000 이라 괜찮은데 while에서 추가적인 시간으로 인한 실패 예상
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    num_list = list(map(int,sys.stdin.readline().split()))
    gcd_list=[]
    for i in range(1,len(num_list)-1):
        for j in range(i+1,len(num_list)):
            a = max(num_list[i],num_list[j])
            b = min(num_list[i],num_list[j])
            gcd=1
            for k in range(2,b+1):
                while a%k==0 and b%k==0:
                    gcd*=k
                    a=a//k
                    b=b//k
            gcd_list.append(gcd)
    print(sum(gcd_list))

#시간 초과 -> combinations 모듈을 이용하여 시간을 줄이려 했으나 위와 같이 while문에서 시간오바 예상
import sys
from itertools import combinations
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    num_list = list(map(int,sys.stdin.readline().split()))
    comb_list=[]
    for i in combinations(num_list[1:],2):
        comb_list.append(list(i))
    gcd_list=[]
    for i in comb_list:
        min_num = (min(i[0],i[1]))
        gcd=1
        for j in range(2,min_num//2+2):
            while i[0]%j==0 and i[1]%j==0:
                    gcd*=j
                    i[0]=i[0]//j
                    i[1]=i[1]//j
        gcd_list.append(gcd)
    print(sum(gcd_list))
   
#다른 풀이 math 모듈의 gcd 이용하면 삼중for문으로 쉽게 해결가능
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
