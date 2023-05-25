import sys
input=sys.stdin.readline
n=int(input())
time_list=list(map(int,input().split()))
time_list.sort()
total_time=0
for i in range(len(time_list)):
    total_time+=time_list[i]*(len(time_list)-i)
print(total_time)