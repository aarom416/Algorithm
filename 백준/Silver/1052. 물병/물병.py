import sys
input=sys.stdin.readline
n,k=map(int,input().split())
stack=[]
n=bin(n)[2:]
total_last_number=0
for i in range(len(n)):
    if n[i]=='1':
        stack.append(2**(len(n)-1-i))
if len(stack)<=k:
    print(0)
    exit()
for _ in range(len(stack)-k):
    total_last_number+=stack.pop()
print(stack[-1]-total_last_number)