import sys

n = int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().split()))
new_list = []

M = max(list)

for i in range(n):
    new_list.append(list[i]/M*100)

print(sum(new_list)/len(new_list))

