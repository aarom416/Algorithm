# 시간 초과 - n의 개수가 1~100,000개여서 O(nlogn)이하 알고리즘을 사용해야 하는데 이중 for문으로 O(n**2)을 사용해서 시간 초과 난거 같음
import sys
n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
num=list(range(1,n+1))
result=[]
stack=[]
print_list=[]
idx=0
for i in num_list:
    for j in range(idx,len(num)):
        if i in stack: #stack에 있는 지 먼저 확인 
            print_list.append('-')
            result.append(stack.pop())
            break
        else:
            if i!=num[j]: #입력한 수와 같은 지 확인하고 없으면 push 있으면 push 후 pop
                stack.append(num[j])
                print_list.append('+')
                idx+=1 #인덱스 기억하고 for문에 넘겨주어 다음 번호부터 확인하도록함
            else: #
                print_list.append('+')
                stack.append(num[j])
                result.append(stack.pop())
                print_list.append('-')
                idx+=1
                break
#idx와 len(num)값이 같아져 for문을 실행하지 않아 stack에 남아있는 수 pop            
for _ in range(len(stack)): 
    result.append(stack.pop())
    print_list.append('-')

if num_list==result:
    for i in print_list:
        print(i)
else:
    print('NO')
    

# 다른 풀이
n = int(input())
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:     
        stack.append(cur)
        answer.append("+")
        cur += 1
    if stack[-1] == num:    
        stack.pop()        
        answer.append("-")
    else:                  
        print("NO")         
        flag = 1      
        break               

if flag == 0:
    for i in answer:
        print(i)
