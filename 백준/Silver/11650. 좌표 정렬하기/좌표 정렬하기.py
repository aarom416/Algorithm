import sys
n = int(sys.stdin.readline().rstrip())
num_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

num_list.sort(key=lambda x:(x[0], x[1])) #lambda를 이용해 x먼저 정렬후, y정렬
for i in range(len(num_list)):
    print(num_list[i][0], num_list[i][1])