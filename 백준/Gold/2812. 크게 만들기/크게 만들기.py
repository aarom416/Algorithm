import sys

input = sys.stdin.readline

n,k = map(int,input().split())

numbers = list(input().rstrip())

stack = []
for number in numbers:
    #스택을 확인하면서 스택의 마지막 값과 새로 들어온 값을 계속 비교해 새로운 값이 더 크면 계속 지워나감
    while stack and stack[-1] < number and k>0:
        k-=1
        stack.pop()
    stack.append(number)
print(''.join(stack[:len(stack)-k])) #k값이 남아있는 경우 k값 만큼 뒷부분 버림