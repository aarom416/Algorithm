def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    for a,b in zip(A,B):
        answer += a*b

    # 첫 풀이 - 시간 초과 O(n^2)
    # for _ in range(len(A)):
    #     min_a = min(A)
    #     max_b = max(B)
    #     answer += min_a*max_b
    #     A.remove(min_a)
    #     B.remove(max_b)
    return answer

## 다른 풀이 - 컴프리헨션 적용 (가독성, 오버헤드)
def solution(A,B):
    return sum([a*b for a,b in zip(sorted(A), sorted(B, reverse=True))])
