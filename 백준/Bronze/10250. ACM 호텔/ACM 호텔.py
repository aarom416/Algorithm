n = int(input())
for i in range(n):
    h,w,n = map(int,input().split())
    room_num = n//h+1
    room_heigh = n%h
    if n%h ==0 : # n 번째와 층 수가 나눠지면 다르게 처리
        room_num = n//h
        room_heigh = h
    print(f"{room_heigh*100+room_num}")