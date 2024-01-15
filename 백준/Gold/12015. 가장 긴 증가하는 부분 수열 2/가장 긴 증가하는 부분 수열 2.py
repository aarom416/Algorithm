import sys

input = sys.stdin.readline
n = int(input().strip())
number_list = list(map(int,input().split()))

result = [number_list[0]]

#이분 탐색
def binary_search(start, end, target):
    while start<=end:
        mid = (start+end)//2
        if result[mid]==target:
            return mid
        elif result[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return start

for i in range(1,n):
    if result[-1]<number_list[i]: #10 20 10 30 20 50 에서 처음 10,20 은 result에 넣음
        result.append(number_list[i])
    else: 
        # result = [10, 20], number_list = [5, 30, 20, 50] 에서 number_list의 5가 더 작으므로 이분탐색하여 
        # result의 들어가야할 인덱스를 찾아 넣어줌 5 넣은 결과 => result = [5,20]
        idx = binary_search(0,len(result)-1,number_list[i])
        result[idx] = number_list[i]
print(len(result))

