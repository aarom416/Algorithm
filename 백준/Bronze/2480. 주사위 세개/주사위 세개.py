import sys

a,b,c = map(int,sys.stdin.readline().split())

if a==b==c:
    print(10000+a*1000)
elif a==b or a==c or b==c:
    if(a==b):
        print(1000+a*100)
    elif(b==c):
        print(1000+b*100)
    else:
        print(1000+c*100)
else:
    d = max(a,b,c)
    print(d*100)            
