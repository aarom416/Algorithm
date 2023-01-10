n = int(input())
hansu_cnt = 0

for i in range(1,n+1):
    num_list = list(map(int,str(i)))
    if i < 100:
        hansu_cnt += 1 #100보다 작은 수는 모두 한수
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]: #각 자릿수가 2개만 같으면 한수
        hansu_cnt += 1
print(hansu_cnt)