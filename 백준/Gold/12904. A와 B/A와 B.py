import sys

input = sys.stdin.readline

first = list(input().rstrip())
end = list(input().rstrip())
temp_end = end[:]

while len(end) != len(first):
    last_string = end[-1]
    if last_string == "A":
        end.pop()
    else:
        end.pop()
        end.reverse()
if first == end:
    print(1)
else:
    print(0)