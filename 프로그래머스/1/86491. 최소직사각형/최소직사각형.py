def solution(sizes):
    
    w_list = []
    h_list = []
    
    for w,h in sizes:
        if w < h:
            w_list.append(h)
            h_list.append(w)
        else:
            w_list.append(w)
            h_list.append(h)
    
    return max(w_list) * max(h_list)


# 다른 풀이 큰수는 왼쪽에 작은 수는 오른쪽에 comprehison
def solution(sizes):
    
return max(max(x) for x in sizes) * max(min(x) for x in sizes)
