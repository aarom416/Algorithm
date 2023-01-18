import sys
n = int(sys.stdin.readline())
member_list = [list(sys.stdin.readline().split()) for _ in range(n)]
member_list.sort(key=lambda x:int(x[0]))

for i in member_list:
    print(i[0],i[1])
