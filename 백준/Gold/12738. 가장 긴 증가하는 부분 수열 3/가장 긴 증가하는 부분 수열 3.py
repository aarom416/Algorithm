import sys

n = int(input())
number_list = list(map(int,input().split()))

stack = [number_list[0]]

def binary_search(target):
    start=0
    end=len(stack)-1
    while start<=end:
        mid = (start+end)//2
        if target<=stack[mid]:
            end = mid - 1
        else:
            start = mid +1
    return start
        
for i in range(1,n):
    if stack[-1] < number_list[i]:
        stack.append(number_list[i])
    else:
        idx = binary_search(number_list[i])
        stack[idx] = number_list[i]
print(len(stack))