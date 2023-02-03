n =int(input())
num = list(range(1,n+1))
sum=1
cnt=0
for i in num:
    sum*=i
a=str(sum)
zero=[]
for i in range(len(a)-1,0,-1):
    if a[i]=='0':
        zero.append(a[i])
    else:
        break
print(len(zero))
