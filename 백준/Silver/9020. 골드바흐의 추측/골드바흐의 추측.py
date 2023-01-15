import sys
def sosu(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

num = list(range(2,10001))
sosu_list=[]
for i in num:
    if sosu(i):
        sosu_list.append(i)

t = int(input())
for _ in range(t):
    number = int(sys.stdin.readline().rstrip())
    left_list = []
    right_list = []
    number_center = number//2
    for i in sosu_list:
        if number_center == i:
            left_list.append(i)
            right_list.append(i)
        elif number_center<i<number:
            right_list.append(i)
        elif number_center>i:
            left_list.append(i)
        
    for i in range(len(right_list)):
        for j in range(len(left_list)):
            if right_list[i]+left_list[j]==number:
                print(f"{left_list[j]} {right_list[i]}")
                break
        else:
            continue
        break
