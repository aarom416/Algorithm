import sys

n = int(sys.stdin.readline())
list = list(map(int,sys.stdin.readline().split()))
search = int(sys.stdin.readline())

print(list.count(search))
