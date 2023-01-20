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
