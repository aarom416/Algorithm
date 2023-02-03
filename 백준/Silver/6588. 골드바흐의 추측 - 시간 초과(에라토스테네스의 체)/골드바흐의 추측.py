#시간 초과 - 시간복잡도 O(N)에 가깝게 해야되는데 O(N^2)
import sys
while True:
    sosu_list=[]
    result=[]
    tmp=0
    n = int(sys.stdin.readline())
    if n==0:
        break
    for i in range(2,n): #O(N*루트(N))
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            sosu_list.append(i)
    a = int(len(sosu_list)**0.5)
    for i in range(0,a+1): #O(N/2*N/2) => O(N^2)
        for j in range(len(sosu_list)-1,a-1,-1):
            if sosu_list[i]+sosu_list[j]==n:
                result.append(sosu_list[i])
                result.append(sosu_list[j])
                tmp+=1
                break
        if tmp>0:
            break
    if tmp>0:
        print(f'{n} = {result[0]} + {result[1]}')
    else:
        print("Goldbach's conjecture is wrong.")

#다른 풀이 - 시간초과 
import sys
while True:
    sosu_list=[]
    result=[]
    tmp=0
    n = int(sys.stdin.readline())
    if n==0:
        break
    for i in range(2,n): #이부분 바꿔야됨
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            sosu_list.append(i)
    for i in sosu_list:
        if n-i in set(sosu_list): #set()에서 in은 시간복잡도 O(1)인 점을 이용
            print(f'{n} = {i} + {n-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")

#다른 풀이 - 에라토스테네스의 체 사용
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
