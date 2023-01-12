x = int(input())
line = 1

while x>line:
    x-=line 
    line+=1
# 이때 x는 해당 line의 몇 번째 숫자인지 됌

if line%2==0:
    top = x #분자
    bottom = line-x+1 #분모
else:
    top = line-x+1 #분자
    bottom = x #분모
print(f"{top}/{bottom}")