n,b = map(int,input().split())
res=''
tmp='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while n!=0:
    res+=str(tmp[n%b])
    n=n//b
print(res[::-1])