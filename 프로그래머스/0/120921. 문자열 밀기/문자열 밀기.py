def solution(A, B):
    answer = 0
    A = list(A)
    
    for _ in range(len(A)):
        if ''.join(A) == B:
            return answer 
    
        last = A.pop()
        A.insert(0, last)

        answer += 1
    return -1