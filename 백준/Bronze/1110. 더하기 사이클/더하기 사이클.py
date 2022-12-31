import sys

n = int(sys.stdin.readline())
num = n # 첫번째 값 저장
count = 0

while True:
    a = n//10
    b = n%10
    c = (a+b)%10
    
    n = (b*10)+c
    count += 1
    if (n==num):
        print(count)
        break