import sys
import collections
input = sys.stdin.readline

string = input().strip()
bomb_string = input().strip()

bomb_length = len(bomb_string)

stack = []
for s in string:
    stack.append(s)
    if ''.join(stack[-bomb_length:]) == bomb_string:
        for _ in range(bomb_length):
            stack.pop()
if len(stack)==0:
    print("FRULA")
else:
    print(''.join(stack))