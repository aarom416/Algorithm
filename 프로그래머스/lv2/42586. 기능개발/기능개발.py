def calu(x, y): 
    cnt=0
    while x<100:
        x+=y
        cnt+=1
    return cnt
def solution(progresses, speeds):
    answer = []
    stack = []
    stack.append(calu(progresses[0],speeds[0]))
    cnt = 1
    for i in range(1,len(progresses)):
        if max(stack) >= calu(progresses[i],speeds[i]):
            cnt += 1
            stack.append(calu(progresses[i],speeds[i]))
        else:
            answer.append(cnt)
            for _ in range(cnt):
                stack.pop()
            stack.append(calu(progresses[i],speeds[i]))
            cnt = 1
    answer.append(len(stack))
    while stack:
        stack.pop()
    return answer