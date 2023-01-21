import sys
n = int(sys.stdin.readline())
a=set()
for i in range(1,n):
    tmp = i
    for j in str(i):
        i+=int(j)
    if n==i: #최초의 생성자 출력
        print(tmp)
        break
else:
    print(0)