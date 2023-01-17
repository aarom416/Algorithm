import sys
n = int(sys.stdin.readline())
num = [0]*10001 # 공간을 미리 설정
for i in range(n): #입력값에 위치한 리스트값 +1
    num[int(sys.stdin.readline().rstrip())]+=1
for i in range(10001):
    if num[i]!=0: 
        for j in range(num[i]):
             #리스트값에 따라 출력값 설정 ex)i=5,num[i]=2 이면 5가 두번 반복됨
             #따라서 5를 2번 반복시켜 출력
            print(i)
            