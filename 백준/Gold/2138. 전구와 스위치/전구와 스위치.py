import sys
input = sys.stdin.readline

n = int(input())
first = list(map(int, input().rstrip()))
end = list(map(int, input().rstrip()))

# 두번쨰 스위치부터 그 전 스위치가 목표하는 답과 비교하여 다르면 현재 스위치를 눌러 i-1,i,i+1 스위치를 바꿔주고, 같으면 넘김
# 그 전 스위치에 상태가 목표하는 상태와 같은지가 중요 -> 순차적으로 스위치를 보기 떄문에 그 전 스위치를 확정시켜놓지 않으면 영영 바뀌지 않음
def change(a,b):
    temp = a[:]
    count=0
    for i in range(1,n):
        if temp[i-1] == b[i-1]:
            continue
        count+=1
        for j in range(i-1,i+2):
            if j<n:
                temp[j] = 1 - temp[j]
    return count if temp == b else 1e9

#첫번째 스위치를 안눌렀을때
result = change(first, end)
#첫번째 스위치를 눌렀을떄
first[0] = 1 - first[0]
first[1] = 1 - first[1]
result = min(result, change(first,end)+1)
print(result if result != 1e9 else -1)