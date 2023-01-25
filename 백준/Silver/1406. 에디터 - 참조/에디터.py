import sys
list1 = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())
list2=[] #리스트 두개 사용
for _ in range(m):
    command = list(sys.stdin.readline().split())
    if command[0]=='P': #커서를 기준으로 문자열 스택 두개에 나누어 담음
        list1.append(command[1])
    elif command[0]=='L':
        if list1:
            list2.append(list1.pop())
    elif command[0]=='D':
        if list2:
            list1.append(list2.pop())    
    else:
        if list1:
            list1.pop()
list1.extend(reversed(list2))
print(''.join(list1))
