import sys

#1,2,3번 기둥 중 1에 위치한 원판이 3에 위치해야함
#1번 기둥은 start, 2번은 end 3번은 sub로 선언
def hanoi_check(n,start,end,sub): 
    if n==1:
        print(start,end)
        return
    hanoi_check(n-1,start,sub,end) #n-1개 원판을 start에서 sub로 먼저 이동
    print(start,end) #start에 있는 한개의 원판 end로 이동
    hanoi_check(n-1,sub,end,start) #마지막으로 n-1개 원판 위치한 sub에서 end로 이동
n = int(sys.stdin.readline())
print(2**n-1)
hanoi_check(n,1,3,2)