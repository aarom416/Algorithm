import sys
def sosu(num): #소수를 검증하는 함수
    for i in range(2,int(num**0.5)+1):
        if num%i==0: #나머지가 0이면 소수가 아니므로 False 리턴
            return False
    return True #반복문이 끝나면 소수이므로 True 리턴 

#시간 초과를 해결하기 위해 대신 문제에서 주어진 범위의 2n까지 미리 소수를 구함
#구한 소수를 리스트에 넣어둠 계산
#미리 계산하기 때문에 시간 절약
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
        

