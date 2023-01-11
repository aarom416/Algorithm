s = list(input())
time = 0

for i in range(len(s)):
    if s[i]<='C':
        time+=3
    elif s[i]<='F':
        time+=4
    elif s[i]<='I':
        time+=5
    elif s[i]<='L':
        time+=6
    elif s[i]<='O':
        time+=7
    elif s[i]<='S':
        time+=8
    elif s[i]<='V':
        time+=9
    elif s[i]<='Z':
        time+=10
    else:
        time+=2
print(time)