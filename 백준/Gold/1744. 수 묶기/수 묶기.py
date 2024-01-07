import sys

n = int(input().strip())
number = [int(input().strip()) for _ in range(n)]

result = 0

minus_number = []
exist_zero = False
plus_number = []
count = 0
for i in number:
    if i == 1: #1은 1*1 보다 1+1이 더 큰 수이므로 따로 count
        count+=1
        continue
    if i<0:
        minus_number.append(i)
    elif i>0:
        plus_number.append(i)
    else:
        exist_zero = True
        
minus_number.sort() #음수 정렬 2,3,4,5 ...
if len(minus_number) % 2 == 0:
    for i in range(0,len(minus_number),2): #짝수 개일때 두개씩 묶어서 곱함
        result += minus_number[i] * minus_number[i+1]
else:
    for i in range(0,len(minus_number)-1,2): #홀수 개일때 마지막 만 남기고 묶어서 곱함
        result += minus_number[i] * minus_number[i+1]
    if not exist_zero: #0이 없으면 마지막 수 더함 (이때 0이 있으면 위 조건문에서 곱해져 0이거나, 무시되기 때문에 없는 경우만 생각)
       result += minus_number[-1]
       
plus_number.sort(reverse=True) #양수 정렬 -5,-4,-2,-1 ...
if len(plus_number) % 2 == 0:
    for i in range(0,len(plus_number),2):
        result += plus_number[i] * plus_number[i+1]
else:
    for i in range(0,len(plus_number)-1,2):
        result += plus_number[i] * plus_number[i+1]
    result += plus_number[-1]

print(result+count)

#다른 풀이
n = int(input())

plus = []
minus = []

result = 0
for i in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        result += num #0,1은 먼저 더해주면 됨

# 정렬
plus.sort(reverse=True)
minus.sort() # ex) -3 -2 -1 

# 양수 묶기
for i in range(0, len(plus), 2):
    if i+1 >= len(plus): #마지막 숫자인 경우
        result += plus[i]
    else:
        result += (plus[i] * plus[i+1])

# 음수 묶기
for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        result += minus[i]
    else:
        result += (minus[i] * minus[i+1])

print(result)
