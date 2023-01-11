a,b = list(map(int,input().split()))
change_num = []
for i in a,b:
    c = i//100
    d = (i-c*100)//10
    e = i%10
    change_num.append(e*100+d*10+c)
print(max(change_num))'

# 다른 풀이
a, b = input().split()
a = int(a[::-1]) #문자열[::-1] 하면 역순
b = int(b[::-1]) 
print(max(a, b))
