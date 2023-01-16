import sys
def sosu(n): #소수를 구하는 함수
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

num = list(range(2,10001)) #주어진 문제 짝수 범위에 따라 미리 소수 검정->시간 절약(입력값에 따라 계속 소수 구할 필요없음)
sosu_list=[]
for i in num:
    if sosu(i):
        sosu_list.append(i)

t = int(input())
for _ in range(t):
    number = int(sys.stdin.readline().rstrip())
    left_list = [] #입력받은 짝수의 절반을 기준으로 왼쪽에 있는 소수 리스트
    right_list = [] #입력받은 짝수의 절반을 기준으로 오른쪽에 있는 소수 리스트
    number_center = number//2 #짝수의 절반
    for i in sosu_list:
        if number_center == i: #모든 소수 중 짝수의 절반값과 같은 소수는 좌우 리스트 모두 추가
            left_list.append(i)
            right_list.append(i)
        elif number_center<i<number: #짝수의 절반보다 크고 짝수보다 작은 소수는 오른쪽 리스트에 추가
            right_list.append(i)
        elif number_center>i: #짝수의 절반보다 작은 소수는 왼쪽 리스트에 추가 
            left_list.append(i)
        #ex) 입력값:11 절반값:5 왼쪽 리스트: 2,3 오른쪽 리스트 7

    #오른쪽 리스트를 기준으로 왼쪽 리스트 0번쨰부터 순서대로 더하면서 입력값과 같은지 확인
    #이렇게 하면 차이가 최소인 소수들로 바로 나옴
    for i in range(len(right_list)): 
        for j in range(len(left_list)):
            if right_list[i]+left_list[j]==number:
                print(f"{left_list[j]} {right_list[i]}") 
                break 
        else: #위에 break가 발생하지 않으면 소수의 합을 찾지 못한 것으로 다시 반복문으로 돌아감
            continue
        break # 이중 for문 break
