import sys
bar = sys.stdin.readline()
cnt=0
bar_stack=[]
for i in range(len(bar)):
    if bar[i]=='(': #'(' 이면 append
        bar_stack.append(bar[i])
    elif bar[i]==')': 
        if bar[i-1]==')': #')'이 연속이면 bar 하나가 끝나므로 마지막 끝부분 +1
            cnt+=1
            bar_stack.pop()
        else: #stack에 남아 있는 개수(=bar의 개수)만큼 count
            bar_stack.pop()
            cnt+=len(bar_stack)
print(cnt)