# O(N) 풀이 - 딕셔너리 사용
def solution(topping):
    answer = 0
    
    brother = {}
    
    for t in topping:
        if t in brother:
            brother[t] += 1
        else:
            brother[t] = 1
    
    chulsoo = {}
    
    for t in topping:
        if t in chulsoo:
            chulsoo[t] += 1
        else:
            chulsoo[t] = 1
            
        brother[t] -= 1
        if brother[t] == 0:
            del brother[t]
            
        if len(brother) == len(chulsoo):
            answer+=1
    return answer


# 처음 풀이 오답 - 범위가 1000000 이하이기 때문에 O(n^2) 로 풀이 하면 시간 초과 -> O(1)의 딕셔너리로 시간 복잡도를 줄이는 방식의 생각 전환이 필요

def solution(topping):
    answer = 0
    
    for i in range(1, len(topping)):
        a,b = topping[:i], topping[i:]
        
        if len(set(a)) == len(set(b)):
            answer += 1
    return answer
