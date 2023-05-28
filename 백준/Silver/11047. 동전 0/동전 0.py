import sys
input=sys.stdin.readline
n,k=map(int,input().split())
coin_list=[int(input().rstrip()) for _ in range(n)]
coin_list.sort(reverse=True)
i=0
answer=0
while k!=0:
    answer+=k//coin_list[i]
    k=k%coin_list[i]
    i+=1
print(answer)