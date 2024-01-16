import sys

input = sys.stdin.readline
n = int(input().strip())
number_list = list(map(int,input().split()))

result = [number_list[0]]

def binary_search(start, end, target):
    while start <= end:
        mid = (start+end)//2
        if result[mid]>=target:
            end = mid-1
        else:
            start = mid+1
    return start
    
for i in range(1,n):
    if result[-1]<number_list[i]:
        result.append(number_list[i])
    else:
        idx = binary_search(0,len(result)-1,number_list[i])
        result[idx] = number_list[i]
print(len(result))

