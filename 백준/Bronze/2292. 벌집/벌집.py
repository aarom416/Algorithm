n = int(input())
bee_cnt = 1
cnt = 1 
while n > bee_cnt:
    bee_cnt += 6*cnt #벌집 개수 6배수만큼 증가
    cnt+=1
print(cnt)