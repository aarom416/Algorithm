import sys

input = sys.stdin.readline

n = int(input())
money_list = list(map(int, input().split()))
k = int(input())
result = 0

start = 0
end = max(money_list)
while start<=end:
    mid = (start+end)//2
    max_money = 0
    for money in money_list:
        max_money+=min(money,mid)
    if max_money <= k:
        start = mid + 1
        result=mid
    else:
        end = mid - 1
print(result)

