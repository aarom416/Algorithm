s1 = input()
answer=[]
a=[]
b=[]

def multi_div(s):
    stack=[]
    result=[]   
    next=0
    for k in s:
        add=''
        cnt=0
        if k=="*" or k=='/':
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
    return result
def puls_minus(s): 
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
    return result[-1]
stack=[]
for i in s1:
    if i==')':
        while True:
            if a[-1]=="(":
                a.pop()
                break
            else:
                stack.append(a.pop())
        if len(stack)==3:
            for i in range(len(stack)):
                b.append(stack[2-i])
            a.append(puls_minus(multi_div(b)))
            b.clear()                
        else:
            stack.reverse()
            a.append(puls_minus(multi_div(stack)))
        stack.clear()
    else:
        a.append(i)
answer.append(puls_minus(multi_div(a)))
print(answer[-1])