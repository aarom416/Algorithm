n,b = map(str,input().split())
b=int(b)
res=0
tmp='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(n)):
    a=tmp.index(n[i])
    res+=a*b**(len(n)-1-i)
print(res)