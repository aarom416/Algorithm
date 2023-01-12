import sys
A,B,V = map(int,sys.stdin.readline().split())
day = (V-B)/(A-B)
print(int(day) if day==int(day) else int(day)+1 )