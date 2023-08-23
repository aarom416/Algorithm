def solution(s):
    answer = []
    for string_list in s:
        stack=[]
        count_110=0
        count_1=0
        # stack 을 사용하여 110의 개수 확인
        for string in string_list:
            if len(stack)>=2 and string=="0" and stack[-1]=='1' and stack[-2]=='1':
                stack.pop()
                stack.pop()
                count_110+=1
            else:
                stack.append(string)
        # 110을 모두 제거하면 연속된 1이 나타나는 지점이 없거나(110 삭제할때 11에 의해 사라짐)
        # 한 지점에만 생김 (ex 0111111010->0110110111)
        # 110을 모두 제외한 나머지 stack을 뒤에서부터 확인하여 1의 개수 확인
        # stack에 남아있는 문자열이 100 인 경우는 이거 그대로 사용하면 되고 0111 인 경우 111보다 110가 앞에 있어야하므로 1의 개수를 세서 뒤쪽으로 보내야함
        for s in stack[::-1]:
            if s=='0':
                break
            else:
                count_1+=1
        answer.append("".join(stack[:len(stack)-count_1])+"110"*count_110+"1"*count_1)
    return answer
