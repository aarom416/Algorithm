upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower= "abcdefghijklmnopqrstuvwxyz"
num='1234567890'
while True:
    try:
        s=input()
        upper_cnt=0
        lower_cnt=0
        num_cnt=0
        null_cnt=0
        for i in s:
            if i in upper:
                upper_cnt+=1
                continue
            elif i in lower:
                lower_cnt+=1
                continue
            elif i in num:
                num_cnt+=1
                continue
            else:
                null_cnt+=1
                continue
        print(lower_cnt,upper_cnt,num_cnt,null_cnt)
    except EOFError:
        break