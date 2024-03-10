import sys

input = sys.stdin.readline
n = int(input())
chu = list(map(int,input().split()))

chu.sort()

#가능한 열린 구간 중 마지막 구간을 나타낼 변수
check = 1 
#만들 수 있는 최소 구간과 최대 구간을 구분
#1 1 2 3 6 7 30 경우
# 1 -> 열린 구간 [0,1] 가능
# 1 -> 열린 구간 [0,1]에서 +1 하여 [1,2] 가능하고 [0,1]에서 [1,2]는 연속 => 최종 [0,2] 가능
# 2 -> 열린 구간 [0,2]에서 +2 하여 [2,4] 가능하고 [0,2]에서 [2,4]는 연속 => 최종 [0,4] 가능
# 3 -> 열린 구간 [0,4]에서 +3 하여 [3,7] 가능하고 [0,4]에서 [3,7]는 연속 => 최종 [0,7] 가능
# 6 -> 열린 구간 [0,7]에서 +6 하여 [6,13] 가능하고 [0,7]에서 [6,13]는 연속 => 최종 [0,13] 가능
# 7 -> 열린 구간 [0,13]에서 +7 하여 [7,20] 가능하고 [0,13]에서 [7,20]는 연속 => 최종 [0,20] 가능
# 30 -> 열린 구간 [0,20]에서 +30 하여 [30,50] 가능하고 [0,20]에서 [30,50]는 불연속 => 21부터 안됨

for i in chu:
    if check<i:
        break
    check+=i
print(check)
