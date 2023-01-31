string = input()
res=''
for i in string:
    if i.isalpha():
        if ord(i)>109:
            res+=chr(ord(i)-13)
        elif ord(i)>=97:
            res+=chr(ord(i)+13)
        elif ord(i)>77:
            res+=chr(ord(i)-13)
        else:
            res+=chr(ord(i)+13)
    else:
        res+=i
print(res)