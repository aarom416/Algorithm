from itertools import permutations

def solution(numbers):
    answer = 0
    
    final_set = set()
    
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            final_set.add(num)
            
    for n in final_set:
        if is_prime(n):
            answer+=1
        
    return answer
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True