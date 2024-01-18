#나의 풀이 (메모리 초과) -> 이중 for문을 돌리가 때문에 n이 10^5 인 경우 메모리 초과가 엄청 날 것으로 예상된다. 또한 O(nlogn)으로 시간복잡도를 잡고 접근해야 한다.
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

stack = []
count=k
def binary_search(start, end, target):
    while start<=end:
        mid = (start+end)//2
        if stack[mid] == target:
            return mid
        elif stack[mid]< target:
            start = mid + 1
        else:
            end = mid - 1
    return start
for i in range(1,n+1):
    for j in range(i,n+1):
        stack.append(i*j)
        count-=1
        if count==0:
            print(stack[-1])
            exit()
        if i==j:
            idx = binary_search(0,len(stack),i*j)
            stack[idx] = i*j
        else:
            stack.append(j*i)
            count-=1
        if count==0:
            print(stack[-1])
            exit()

#다른 풀이 - 메모리 초과가 나는 것을 방지하기 위해 k번째보다 작은 값이 몇 개인지 확인하는 식으로 접근
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

def binary_serach(start, end, target):
    while start<=end:
        mid = (start+end)//2 #특정수 mid 
        cnt = 0
        for i in range(1,n+1): #특정수 mid 보다 작은 수들이 총 몇 개인지 확인
            cnt += min(mid//i,n) #특정수를 1부터 나눠서 몇 개인지 각 몇 개인지 확인할때 n개를 넘으면 안됨
        if cnt >= target: #특정 수보다 작은 숫자의 개수가 k번째보다 큰 경우 -> k번째를 넘어간 것이므로 end를 내림
            end = mid - 1
        else:
            start = mid + 1 #특정 수보다 작은 숫자의 개수가 k번째보다 작은 경우 -> k번째 안에 있으모로 start를 올림
    return start
print(binary_serach(0,n*n,k))
