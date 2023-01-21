import sys
n,m = map(int,sys.stdin.readline().split())
result=[]
card_list = list(map(int,sys.stdin.readline().split()))
for i in range(0,len(card_list)):
    for j in range(i+1,len(card_list)):
        for k in range(j+1,len(card_list)):
            if card_list[i]+card_list[j]+card_list[k]>m:
                continue
            else:
                result.append(card_list[i]+card_list[j]+card_list[k])
print(max(result))                

#다른 풀이

from itertools import combinations #combinations 함수 사용
card_num, target_num = map(int, input().split())
card_list = list(map(int,input().split()))
biggest_num=0
for cards in combinations(card_list,3): #입력값을 3개의 모든 조합 만듬
    temp_sum = sum(cards)
    if biggest_num<temp_sum<=target_num: #제일 목표값과 가까운 값 찾기
        biggest_num = temp_sum         
print(biggest_num)     
