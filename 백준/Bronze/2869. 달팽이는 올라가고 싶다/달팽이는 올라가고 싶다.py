import sys
A,B,V = map(int,sys.stdin.readline().split())
day = 1
heigh = 0
while True:
    max_heigh = heigh - A
    heigh += A-B
    if max_heigh>=V:
        print(day)
        break
    day+=1
# 답은 되지만 while 문으로 인해 시간 초과    

# 다른 풀이 (while 문X)
import sys
A,B,V = map(int,sys.stdin.readline().split())
day = (V-B)/(A-B) # A*day - B*(day-1) = V 이 식을 이항시켜 한번에 day 구함
print(int(day) if day==int(day) else int(day)+1 ) 
# ex) 삼항연산자를 사용하여 day=4.1 이면 하루 더 필요하므로 day+1, day=4.0이면 day를 출력
