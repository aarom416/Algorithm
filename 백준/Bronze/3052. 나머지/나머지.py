import sys

num=[]
cnt = 0

list = [int(sys.stdin.readline()) for _ in range(10)]

for i in range(10):
    num.append(list[i]%42)
   
print(len(set(num)))