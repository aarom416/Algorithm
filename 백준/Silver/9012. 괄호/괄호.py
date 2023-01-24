n = int(input())
for _ in range(n):
    string = input()
    stack=[]
    for i in string:
        if i=='(': # '(' 인 경우만 추가
            stack.append(i)
        else: # ')' 인 경우 
            if len(stack)==0: #현재 스택이 비어 있으면 NO
                print('NO')
                break
            else:
                stack.pop() #현재 스택이 있으면 pop하여 '(' 와 짝을 이루어 없앰
                if len(stack)==0: #이때 스택이 비어진다해도 계속 수행함
                    continue
    else: 
        if len(stack)==0: #현재 스택이 모두 짝을 이룬 경우
            print('YES')
        else: #현재 스택이 남아 있어 짝을 이루지 못한 경우
            print('NO')