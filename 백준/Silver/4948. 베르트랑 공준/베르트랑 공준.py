import sys
def sosu(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

number = list(range(2,246912))
sosu_list = []
for i in number:
    if sosu(i):
        sosu_list.append(i)

while True:
    sosu_cnt = 0
    n = int(sys.stdin.readline().rstrip())
    if n==0:
        break
    for i in sosu_list:
        if n<i<=n*2:
            sosu_cnt+=1
    print(sosu_cnt)
        

