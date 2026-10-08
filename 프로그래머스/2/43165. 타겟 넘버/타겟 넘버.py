def solution(numbers, target):
    
    count = 0
        
    def dfs(idx, total):
        nonlocal count        
        if idx == len(numbers):
            if total == target:
                count += 1
            return
        dfs(idx+1, total + numbers[idx])
        dfs(idx+1, total - numbers[idx])
        
    dfs(0,0)
    return count