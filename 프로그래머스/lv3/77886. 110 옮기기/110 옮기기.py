def solution(s):
    answer = []
    for string_list in s:
        stack=[]
        count_110=0
        count_1=0
        for string in string_list:
            if len(stack)>=2 and string=="0" and stack[-1]=='1' and stack[-2]=='1':
                stack.pop()
                stack.pop()
                count_110+=1
            else:
                stack.append(string)
        for s in stack[::-1]:
            if s=='0':
                break
            else:
                count_1+=1
        answer.append("".join(stack[:len(stack)-count_1])+"110"*count_110+"1"*count_1)
    return answer