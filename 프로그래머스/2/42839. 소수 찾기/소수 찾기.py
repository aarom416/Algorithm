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


## 다른 풀이 백트리캥 + 슬라이싱
number_set = set()

def solution(numbers):
    
    makeCombinations("", numbers)
    
    answer = len(number_set)
    
    return answer

def makeCombinations(str1, str2):
    if str1 and is_prime(int(str1)):
        number_set.add(int(str1))
        
    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i+1:])
        
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
