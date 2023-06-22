def solution(numbers, target):
    sub_node=[0] #처음 0부터 시작 
    for i in numbers:
        stack=[]
        # 트리를 사용하여 각 숫자에 +,- 부분으로 서브트리를 구성하며 만들면 됨
        for node in sub_node:
            stack.append(node+i)
            stack.append(node-i)
        sub_node=stack #구성한 잎들에 대해 다시 +,- 해줘야 하므로 sub_node로 넘김
    count=0
    for i in sub_node: #구성한 트리에서 target 있는지 확인
        if i==target:
            count+=1
    return count