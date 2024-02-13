import sys

input = sys.stdin.readline

n = int(input())

stars = list(map(int, input().split()))

min_dp = stars
max_dp = stars

for _ in range(n-1):
    stars = list(map(int, input().split())) #슬라이싱 윈도우 - 사용하지 않은 값은 배열에 저장하지 않고 배열을 게속 새롭게 갱신
    min_dp = [stars[0]+min(min_dp[0],min_dp[1]), stars[1]+min(min_dp[0],min_dp[1],min_dp[2]), stars[2]+min(min_dp[1],min_dp[2])]
    max_dp = [stars[0]+max(max_dp[0],max_dp[1]), stars[1]+max(max_dp[0],max_dp[1],max_dp[2]), stars[2]+max(max_dp[1],max_dp[2])]
print(max(max_dp),min(min_dp))