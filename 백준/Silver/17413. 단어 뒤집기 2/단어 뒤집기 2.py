import sys
words = sys.stdin.readline().rstrip()
a=[] #결과값을 넣는 리스트
b=[] #뒤집을 값을 넣는 리스트
length=len(words)
i=0
while length>0: #단어 길이까지 반복
    if words[i]=='<': 
        while len(b)>0: #뒤집을 값이 있는지 확인
            a.append(b.pop())
        while True: #없으면 '>' 만날때 까지 순서대로 append
            if words[i]=='>':
                a.append(words[i])
                i+=1
                length-=1
                break
            else:
                a.append(words[i])
                i+=1
                length-=1
    else: #<>안에 있는 문자 아니면 뒤집어 놓을 문자이므로
        if words[i]==' ': #' '이면 b에 append 한 문자 pop 
            while len(b)>0:
                a.append(b.pop())
            a.append(' ') #' ' 추가
            i+=1
            length-=1
        else:
            b.append(words[i]) #뒤집어 놓을 문자 append
            i+=1
            length-=1
if b: #마지막에 '<'를 만나지 않을떄 b에 남아있는 문자열 모두 뒤집음 ex)<max>7085774586302733229
    for j in range(len(b)):
        a.append(b.pop())
for k in a:
    print(k, end="")