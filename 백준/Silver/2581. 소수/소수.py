m,n = [int(input()) for _ in range(2)]

sosu_list = []
for i in range(m,n+1):
    error = 0
    if i>1:
        for j in range(2,i): #2부터 나눠서 소수판단
            if i%j == 0: #나머지가 0이면 소수가 아니므로 error 카운트
                error += 1
        if error == 0: #error가 0이면 소수이므로 리스트에 append
            sosu_list.append(i)
    else: #1은 소수가 아니므로 pass
        pass
if len(sosu_list)==0: #리스트 개수가 0이면 -1, 아니면 합과 최솟값 출력
    print(-1)
else:
    print(sum(sosu_list))
    print(min(sosu_list))
