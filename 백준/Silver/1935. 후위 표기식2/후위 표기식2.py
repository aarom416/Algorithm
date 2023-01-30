n = int(input())
words = input()
string={} #딕셔너리 사용
stack=[]
word = sorted(list(set(words)))
for i in word:
    if i=='+' or i=='-' or i=='*' or i=='/':
        pass
    else:
        string[i]=int(input())
for i in words:
    if i=='+':
        a=stack.pop()
        b=stack.pop()
        stack.append(a+b)
    elif i=='-':
        a=stack.pop()
        b=stack.pop()
        stack.append(b-a)
    elif i=='*':
        a=stack.pop()
        b=stack.pop()
        stack.append(a*b)
    elif i=='/':
        a=stack.pop()
        b=stack.pop()
        stack.append(b/a)
    else:
       stack.append(string.get(i))
print(f'{stack[-1]:.2f}')