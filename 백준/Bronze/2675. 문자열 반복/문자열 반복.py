n = int(input())
for i in range(n):
    s = list(input().split())
    string = list(s[1])
    for i in string:
        print((i*int(s[0])), end='')
    print()