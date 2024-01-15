import sys

input = sys.stdin.readline
n = int(input().strip())
first_number_list = list(map(int,input().split()))
m = int(input().strip())
second_number_list = list(map(int,input().split()))

first_number_list.sort()

def binary_search(number_list, target, start, end):
    while start<=end:
        mid = (start+end)//2
        
        if number_list[mid]==target:
            print(1)
            return
        elif number_list[mid]>target:
            end=mid-1
        else:
            start=mid+1
    print(0)
    
for target in second_number_list:
    binary_search(first_number_list, target, 0, n-1)