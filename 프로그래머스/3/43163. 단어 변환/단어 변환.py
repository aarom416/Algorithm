def solution(begin, target, words):
    answer = float('inf')
    
    visited = {}
    
    alpha = {
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
    }
    
    for word in words:
        visited[word] = False
            
    def dfs(word, count):
        
        nonlocal answer
        
        if word == target:
            answer = min(answer, count)
            return 
        
        for i in range(len(word)):
            for a in alpha:
                temp = list(word)
                temp[i] = a
                next_word = ''.join(temp)
                if next_word in visited and not visited[next_word]:
                    visited[next_word] = True
                    dfs(next_word, count+1)
                    # 백트래킹
                    visited[next_word] = False
    
    dfs(begin, 0)
    
    if answer == float('inf'):
        return 0
    return answer