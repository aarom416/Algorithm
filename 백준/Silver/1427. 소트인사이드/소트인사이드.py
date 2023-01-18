import sys
n = sys.stdin.readline().rstrip()
num_list = []
for i in n:
    num_list.append(i)
num_list = list(map(int, num_list))
num_list.sort(reverse=True)
for i in num_list:
    print(i,end="")