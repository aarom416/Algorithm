def solution(n):
    answer = 1
    i = 1
    while answer*i < n:
        i += 1
        answer *= i
    return i