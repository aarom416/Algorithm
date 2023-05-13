import sys
input=sys.stdin.readline
n,k=map(int,input().split())
stack=[]
n=bin(n)[2:] #13->ob1101 에서 1101 만 가져옴
total_last_number=0
for i in range(len(n)):
    if n[i]=='1': #13 2 인 경우 1101에서 stack에 8,4,1 저장
        stack.append(2**(len(n)-1-i))
if len(stack)<=k: #이때 13 3 이나 13 5 처럼 구성 원소가 8,4,1 3개인데 k=3 이면 물병 안사도 되고 k=5되면 구성할 수 없으므로 0 출력
    print(0)
    exit()
#8,4,1에서 물병 1개 사면 8,4,1,1->8,4,2 물병 1개 더 사면 8,4,2,1 하나 더 사면 8,4,2,1,1->8,4,2,2->8,4,4->8,8 이므로 3개 사야함
#따라서 k개의 물병으로 물을 맞추기 위해선 stack의 구성원소 개수에서 k개를 뺀 개수를 pop() 하여 더해놓고 stack의 마지막 값과 더해놓은 값을 뺴면 됨
#(13,2 경우 stack의 구성원소 [8,4,1] k=2이므로 stack의 구성원소 개수 3에서 k=2를 빼면 1이므로 pop()을 한번한 값을 total_last_number로 받고
#이때 total_last_number=1 그 후 stack의 마지막 값 4와 total_last_number=1 을 뺴면 3이 나옴 -> 물병을 3개 사야 8,4,1 중 1과 합체된 후 4까지 합체되어 k=2를 구성할 수 있게 됨
#1000000 5 경우 stack 구성원소 = [524288, 262144, 131072, 65536, 16384, 512, 64] => 7개 7-5=2 이므로 2개 pop()하고 pop()한 값끼리 더함 -> 576
#pop() 한 후 stack = [524288, 262144, 131072, 65536, 16384] stack의 마지막 값 16384-576(pop한거 다 더한값)=15808
for _ in range(len(stack)-k): 
    total_last_number+=stack.pop()
print(stack[-1]-total_last_number)