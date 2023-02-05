import sys
n = int(sys.stdin.readline().rstrip())
num = [True for _ in range(1000001)] 
for i in range(2,len(num)): #에네스토스의 체
    if num[i]:
        for j in range(i+i,1000001,i):
            num[j]=False
for i in range(n):
    number = int(sys.stdin.readline().rstrip())
    cnt=0
    for j in range(2,number//2+1):
        if num[j] and num[number-j]:
            cnt+=1
    print(cnt)