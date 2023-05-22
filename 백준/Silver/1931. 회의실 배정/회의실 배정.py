import sys
input=sys.stdin.readline
n=int(input())
meeting_list=list()
count=1
# (1 1) (1 1) (1 1) => 3 나와야함
for _ in range(n):
    a,b=map(int,input().split())
    meeting_list.append([a,b])
#끝나는 시간을 기준으로 정렬하고 끝나는 시간이 같으면 시간 시간을 기준으로 정렬
# (2 2), (1 2) 경우 (1 2) (2 2) 되서 count=2 되야 하는데 끝나는 시간만 정렬하면 (2 2) (2 1) 로 되서 count=1 됨 
meeting_list.sort(key=lambda x:(x[1],x[0])) 
end_time=meeting_list[0][1]
for i in range(1,len(meeting_list)):
    if meeting_list[i][0]>=end_time:
        count+=1
        end_time=meeting_list[i][1]
print(count)