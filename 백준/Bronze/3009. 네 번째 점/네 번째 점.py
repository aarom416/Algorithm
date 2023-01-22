num_list = [list(map(int,input().split())) for _ in range(3)]
x=[]
y=[]
for i in range(3):
    x.append(num_list[i][0])
    y.append(num_list[i][1])
for i in x:
    if x.count(i)==1:
        a=i
for i in y:
    if y.count(i)==1:
        b=i
print(a,b)