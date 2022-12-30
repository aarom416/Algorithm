import sys

A,B,C = map(int,sys.stdin.readline().split())
print(f"{(A+B)%C}")
print(f"{((A%C) + (B%C))%C}")
print(f"{(A*B)%C}")
print(f"{((A%C) * (B%C))%C}")