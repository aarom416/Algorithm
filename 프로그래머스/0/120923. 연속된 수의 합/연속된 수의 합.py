def solution(num, total):

    n = (total - sum(range(num)))//num
        
    return [n+i for i in range(num)]