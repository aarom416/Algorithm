a=[0 for _ in range(9) for _ in range(9)]
max_list=[]
idx_list=[]
for i in range(9):
        a[i] = list(map(int,input().split()))
        max_list.append(max(a[i]))
        idx_list.append(a[i].index(max(a[i])))
print(max(max_list))
print(f"{max_list.index(max(max_list))+1} {idx_list[max_list.index(max(max_list))]+1}")