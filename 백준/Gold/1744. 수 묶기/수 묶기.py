import sys

n = int(input().strip())
number = [int(input().strip()) for _ in range(n)]

result = 0

minus_number = []
exist_zero = False
plus_number = []
count = 0
for i in number:
    if i == 1:
        count+=1
        continue
    if i<0:
        minus_number.append(i)
    elif i>0:
        plus_number.append(i)
    else:
        exist_zero = True
        
minus_number.sort()
if len(minus_number) % 2 == 0:
    for i in range(0,len(minus_number),2):
        result += minus_number[i] * minus_number[i+1]
else:
    for i in range(0,len(minus_number)-1,2):
        result += minus_number[i] * minus_number[i+1]
    if not exist_zero:
       result += minus_number[-1]
       
plus_number.sort(reverse=True) 
if len(plus_number) % 2 == 0:
    for i in range(0,len(plus_number),2):
        result += plus_number[i] * plus_number[i+1]
else:
    for i in range(0,len(plus_number)-1,2):
        result += plus_number[i] * plus_number[i+1]
    result += plus_number[-1]

print(result+count)