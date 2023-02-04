import sys,math
import sys
n,s=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
a_list=[]
for i in a:
    if s>i:
        a_list.append(s-i)
    else:
        a_list.append(i-s)
print(math.gcd(*a_list)) #gcd()안에 10,20 처럼 값만 들어가야 하므로 list unpacking해서 [] 없앰
