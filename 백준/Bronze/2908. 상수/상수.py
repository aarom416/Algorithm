a,b = list(map(int,input().split()))
change_num = []
for i in a,b:
    c = i//100
    d = (i-c*100)//10
    e = i%10
    change_num.append(e*100+d*10+c)
print(max(change_num))