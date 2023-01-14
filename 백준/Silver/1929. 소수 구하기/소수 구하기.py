m,n = map(int,input().split())
sosu_list =[]
for i in range(m,n+1):
    if i==1:
        continue
    for j in range(2,int(i**0.5)+1): 
        #range(2,i)하면 필요없는 부분까지 확인함->시간초과
        #특정 수의 제곱근을 구해 제곱근까지의 약수를 구하면 해당 약수를 포함하는 수를 제거하여
        #필요없는 부분까지 읽지 않음
        if i%j == 0:
            break
    else:
        print(i)
