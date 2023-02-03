import sys
n,m = map(int,sys.stdin.readline().split())
#2*5인 개수 찾기
def two_cnt(n):
    two=0
    while n!=0:
        n=n//2 #ex)n=8, 2=2*1, 4=2*2, 6=2*3, 8=2*2*2 2의 개수 7개 
        two+=n
    return two
def five_cnt(n):
    five=0
    while n!=0:
        n=n//5
        five+=n
    return five
#nCm => n!/(n-m)!m! 사용
print(min(two_cnt(n)-two_cnt(n-m)-two_cnt(m),five_cnt(n)-five_cnt(n-m)-five_cnt(m)))