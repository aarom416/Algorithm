import sys

input = sys.stdin.readline

n = int(input())
number_list = list(map(int,input().split()))
number_list.sort()
result=0

def two_pointer(number_list, target):
    start = 0
    end = len(number_list)-1
    while start<end:
        if number_list[start]+number_list[end]==target:
            return 1
        elif number_list[start]+number_list[end]<target:
            start+=1
        else:
            end-=1
    return 0
for i in range(n):
    result+=two_pointer(number_list[:i]+number_list[i+1:], number_list[i])
print(result)