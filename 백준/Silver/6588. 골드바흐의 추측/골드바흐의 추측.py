import sys
sosu_list = [True for _ in range(1000001)] 
for i in range(2, 1001): #에라토스테네스의 체
    if sosu_list[i]: 
        for j in range(i+i,1000001,i): #각 배수만큼 False 
            sosu_list[j]=False #반복문 다 마무리 하고 남아있는 True 는 소수
    
while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    for i in range(3, len(sosu_list)):
        if sosu_list[i] and sosu_list[n-i]:
            print(f'{n} = {i} + {n-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")