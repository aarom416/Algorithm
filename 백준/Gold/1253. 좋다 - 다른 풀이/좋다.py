#나의 풀이 - 런타임 약 1000ms
import sys

input = sys.stdin.readline

n = int(input())
number_list = list(map(int,input().split()))
number_list.sort()
result=0
#투 포인터 사용
for i in range(n):
    target = number_list[i]
    start = 0
    end = len(number_list)-1
    while start<end:
        if number_list[start]+number_list[end]==target:
            #start, end 값이 target의 인덱스와 같으면 안되기 떄문에 조건문 처리 ex) start=0, end=1, target=1 인 경우
            if start == i: 
                start += 1
            elif end == i:
                end -= 1
            else:
                result+=1
                break
        elif number_list[start]+number_list[end]<target:
            start += 1
        else:
            end -= 1
print(result)

#다른 풀이 - 런타임 약 500ms
#처음 풀이와 동일하게 투 포인터를 사용하지만 start, end 값이 0인 경우 위 코드에서 추가적으로 사용한 조건문 처리를 생략하기 위해 
#target 인덱스에 위치한 값을 제외하여 리스트를 파라미터로 보냄 
#위 코드보다 런타임이 약 반으로 줄어든 이유는 target을 제외하고 슬라이싱한 리스트를 파라미터로 보내기 때문에 추가적인 탐색 연산을 할 필요가 없기 때문이라고 예상
#하지만 슬라이싱은 리스트 복사를 위한 연산과 추가적인 메모리를 요구하기 떄문에 이 문제 상황에서는 좋은 성능을 보였지만 무조건 좋은 방법이라고 할 수 없다고 생각
import sys

input = sys.stdin.readline

n = int(input())
number_list = list(map(int,input().split()))
number_list.sort()
result=0

#투 포인터 사용
def two_pointer(number_list, target):
    start = 0
    end = len(number_list)-1
    while start<end:
        if number_list[start]+number_list[end]==target:
            return 1
        elif number_list[start]+number_list[end]<target:
            start+=1
        else:
            end-=1
    return 0
for i in range(n):
    #위에 추가적인 조건문 처리를 생략하기 위해 target 인덱스에 위치한 값을 제외한 리스트를 파라미터로 보냄
    result+=two_pointer(number_list[:i]+number_list[i+1:], number_list[i]) 
print(result)
