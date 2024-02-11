t = int(input())

for _ in range(t):
    k = int(input())
    pages = [0] + list(map(int,input().split()))

    sum_list = [0 for _ in range(k+1)]

    #누적합 
    for i in range(1,k+1): 
        sum_list[i] = sum_list[i-1] + pages[i]

    dp = [[0 for i in range(k+1)] for j in range(k+1)]

    for i in range(2,k+1):
        for j in range(1,k+2-i):
            dp[j][j+i-1] = min([dp[j][j+q] + dp[j+q+1][j+i-1] for q in range(i-1)]) +(sum_list[j+i-1] - sum_list[j-1])
    print(dp[1][k])