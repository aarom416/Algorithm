import sys
n = int(sys.stdin.readline())
weight_heigh = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
rank_list=[]
for i in range(n):
    rank=1
    for j in range(n):
        if weight_heigh[i][0] < weight_heigh[j][0] and  weight_heigh[i][1] < weight_heigh[j][1]:
            rank+=1
    rank_list.append(rank)
for i in rank_list:
    print(i,end=' ')