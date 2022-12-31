import sys

# list comprehension 으로 입력받을 때(엔터로 입력받음)
list = [int(sys.stdin.readline()) for _ in range(9)]

# for문으로 입력받을 때 (엔터로 입력받음)
# list=[]
# for i in range(9):
#     i = int(sys.stdin.readline())
#     list.append(i)

print(max(list))
print(list.index(max(list))+1)