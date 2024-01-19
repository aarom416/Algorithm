import sys

input = sys.stdin.readline

n = int(input())
number_list = list(map(int,input().split()))
number_list.sort()
result=0
#투 포인터 사용
for i in range(n):
    target = number_list[i]
    start = 0
    end = len(number_list)-1
    while start<end:
        if number_list[start]+number_list[end]==target:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                result+=1
                break
        elif number_list[start]+number_list[end]<target:
            start += 1
        else:
            end -= 1
print(result)