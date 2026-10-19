def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    for a,b in zip(A,B):
        answer += a*b
    # for _ in range(len(A)):
    #     min_a = min(A)
    #     max_b = max(B)
    #     answer += min_a*max_b
    #     A.remove(min_a)
    #     B.remove(max_b)
    return answer