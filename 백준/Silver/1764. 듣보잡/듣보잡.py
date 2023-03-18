import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dic={}
for _ in range(n):
    dic[input().rstrip()]=1 #듣도 못한 사람 {이름:1}로 체크
for i in range(m):
    a=input().rstrip() #보도 못한 사람 체크
    if a in dic: #보도 못한 사람 이름 중에 듣도 못한 사람 이름 존재하면 
        dic[a]+=1 #값 증가
    else: #존재하지 않으면 
        dic[a]=1 #1로 체크
cnt=0
stack=[]
for i in dic.keys():
    if dic[i]==2: #key값이 2인 듣보잡인 사람 수 체크
        cnt+=1
        stack.append(i)
stack.sort() #사전순 배열
print(cnt)
for i in stack:
    print(i)