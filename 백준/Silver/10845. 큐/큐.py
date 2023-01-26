from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())
x = deque()
y = deque()
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0]=='push':
        x.append(command[1])
    elif command[0]=='pop':
        if len(x)==0:
            print(-1)
        else:
            print(x.popleft())
    elif command[0]=='size':
        print(len(x))
    elif command[0]=='empty':
        if len(x)==0:
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if x:
            print(x[0])
        else:
            print(-1)
    else:
        if x:
            print(x[-1])
        else:
            print(-1)