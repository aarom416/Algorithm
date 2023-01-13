n = int(input())
num_list = list(map(int,input().split()))

list_cnt = len(num_list)
for i in range(list_cnt):
    cnt = 0
    if num_list[i]==1: #1은 소수가 아니므로 제외
        list_cnt-=1
    else:
        if num_list[i]==2: #2는 소수이므로 제외할 필요 없음
            pass
        else: #1,2 아닌 숫자 중 소수가 아닌 수 전체에서 제외
            for j in range(2,num_list[i]):
                if num_list[i]%j==0:
                    cnt+=1
            if cnt>0:
                list_cnt -= 1
print(list_cnt)