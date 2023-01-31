s1 = input()
answer=[]
a=[]
b=[]
def multi_div(s): # *,/ 연산자 처리하는 함수
    stack=[] #후위 연산을 처리하기 위한 리스트
    result=[] #마무리 된 연산을 삽입하기 위한 리스트
    next=0
    for k in s:
        if k=="*" or k=='/':
            next=1
            result.append(k)
        else:
            result.append(k) 
            if next==1: #이때 항상 2개의 피연산자와 1개의 연산자가 result에 존재
                for _ in range(3): #stack에 넣어 처리 후 다시 result에 삽입
                    stack.append(result.pop())
                result.append(stack[2]+stack[0]+stack[1])
                #ex) result=[A,*,C], stack=[C,*,B] => result=[BC*]
                stack.clear() #ex)stack=[]
                next=0
    return result #+,-는 처리 안됐으므로 리스트로 리턴
def puls_minus(s): #+,- 연산자 처리하는 함수, 위 함수와 동일
    stack=[]
    result=[]   
    next=0
    for k in s:
        if k=="+" or k=='-':
            next=1
            result.append(k)
        else:
            result.append(k)
            if next==1:
                for _ in range(3):
                    stack.append(result.pop())
                result.append(stack[2]+stack[0]+stack[1]) 
                stack.clear()
                next=0
    return result[-1] #모든 과정이 끝났기 때문에 리스트에 하나의 값만 존재
stack=[] #후위 연산을 처리하기 위한 리스트
for i in s1:
    if i==')': # 괄호를 우선적으로 처리
        while True:
            if a[-1]=="(":
                a.pop()
                break
            else:
                stack.append(a.pop())
        if len(stack)==3: #괄호에 하나의 연산만 있는 경우 ex) (A+B)
            for i in range(len(stack)):
                b.append(stack[2-i]) #원래 순서로 바꾸고 함수처리
            a.append(puls_minus(multi_div(b)))
            b.clear()                
        else: #괄호에 여러 연산만 있는 경우 ex) (A+B+C-D..)
            stack.reverse() #a에서 pop했으므로 stack에는 반대로 append 되어 있어서 순서대로 만들고 함수 처리
            a.append(puls_minus(multi_div(stack))) #*,/를 우선적으로 처리
        stack.clear()
    else:
        a.append(i)
answer.append(puls_minus(multi_div(a))) #괄호 연산이 없으면 순서대로 함수처리
print(answer[-1])

#다른 풀이
strn = list(input())
stack=[]
res=''
for s in strn:
    if s.isalpha():
        res+=s
    else:
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                res += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                res+= stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack :
    res+=stack.pop()
print(res)
