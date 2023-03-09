n = int(input())
num = list(map(int,input().split()))
stack = list(range(1,len(num)+1)) #순서를 나타내는 stack 리스트
answer = [] #결과 리스트
i = 0 #항상 1먼저 뽑으므로 인덱스 0 설정
idx = num.pop(i) #1번의 종이의 값 뽑음
answer.append(stack.pop(i)) #순서를 결과 리스트에 저장
while num:
    if idx > 0: #종이의 값이 양수면 
        i = (i+idx-1) % len(num) #오른쪽으로 리스트 확인->pop 을 사용하여 원소를 하나 제거했으므로 인덱스값에 -1
    else:
        i = (i+idx) % len(num) #왼쪽으로 리스트 확인->왼쪽부터 확인하므로 -1 안해도 됨
    idx = num.pop(i) #다음 종이의 값 저장 
    answer.append(stack.pop(i)) #순서 반영 
print(*answer) #결과 리스트 unpacking
