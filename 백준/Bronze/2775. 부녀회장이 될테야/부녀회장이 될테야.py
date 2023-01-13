t = int(input())

for i in range(t):
    k,n = [int(input()) for _ in range(2)]
    floor = list(range(1,n+1))
    next_floor = [0]*n
    if k==0:
        print(n)
    else:
        for _ in range(k):
            for u in range(n):
                next_floor[u] = sum(floor[:u+1])
            floor.clear()
            floor.extend(next_floor)
    print(floor[len(floor)-1])