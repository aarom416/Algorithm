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
            