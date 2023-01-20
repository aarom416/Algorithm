import sys

def make_star(n):
    if n==1:
        return ['*']
    star = make_star(n//3) #재귀함수 사용
    a=[]
    for i in star: 
        a.append(i*3)
    for i in star:
        a.append(i+" "*(n//3)+i)
    for i in star:
        a.append(i*3)    
    return a
num = int(sys.stdin.readline())
print('\n'.join(make_star(num)))